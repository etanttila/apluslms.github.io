#!/usr/bin/env python3

"""
Update script for index.md, which contains a list of contributors.

Mappings from emails to github users and real name fixes are not included in
the repo and are kept in a safe place. Mappings can be recreated with a bit of
knowledge and reading commit messages (many have real names there).

The file `update_contributors_local.json` looks something like this:

    {
        "github_token": "...",
        "emails_to_github_users": {
            "user@example.com": "github-user"
        },
        "github_users_to_names": {
            "github-user": "A real name"
        },
        "included_anonymous": [
            "Another real name"
        ]
    }

Web requests are cached to `update_contributors_cache.sqlite`. To reset the
cache, remove the file: `rm update_contributors_cache.sqlite`.

The script usage:

    pip3 install --user -r update_contributors_requirements.txt
    python3 update_contributors,py

"""

import json
import locale
import os.path
import re

import requests
import requests_cache

requests_cache.install_cache('update_contributors_cache')


ORGANIZATIONS = (
    'apluslms',
)

IGNORED_AUTHORS = {
    'root',
    'none',
    'aplus@plus.cs.hut.fi',
    'rubyric@rubyric.com',
    'jutut@jutut.cs.hut.fi',
}
IGNORED_USER_IDS = {
    'github:dependabot[bot]',
}

IGNORED_DOMAINS = {
    'org.aalto.fi',
}

REALNAMES = {
    'Qianqian Qin': '覃茜茜',
    'Ruiyang Ding': '丁瑞洋',
}

emails_to_github_users = {}
github_token = None
github_users_to_names = {}
included_anonymous = ()

try:
    with open('update_contributors_local.json', 'r') as f:
        local_config = json.loads(f.read())
except FileNotFoundError:
    print("WARNING: no local configuration found 'update_contributors_local.json'")
else:
    emails_to_github_users = local_config.get('emails_to_github_users', emails_to_github_users)
    github_token = local_config.get('github_token')
    github_users_to_names = local_config.get('github_users_to_names', github_users_to_names)
    included_anonymous = set(local_config.get('included_anonymous', included_anonymous))


class Github:
    API = 'https://api.github.com'

    def __init__(self, token=None):
        self.users = {}
        self.session = requests.Session()
        if token:
            self.session.headers.update({
                'Authorization': f"token {token}",
            })
        else:
            print("  WARNING: creating Github client without api token!")

    def ratelimit(self):
        return self.session.get(f'{self.API}/rate_limit').json()['rate']

    def get_user(self, obj):
        if not isinstance(obj, dict):
            raise ValueError(f"`obj` is not type of a dict: {obj}")
        if obj['type'] == 'Anonymous':
            if obj['email'] in emails_to_github_users:
                login = emails_to_github_users[obj['email']]
                obj['url'] = f"{self.API}/users/{login}"
                obj['_anon_'] = True
            else:
                return {
                    'provider': None,
                    'id': 'email:' + obj['email'],
                    'name': obj['name'],
                    'email': obj['email'],
                }
        elif obj['type'] in ('User', 'Bot'):
            login = obj['login']
        else:
            raise Exception("Unknown user type: " + obj['type'])
        # resolve github login to user object
        if login not in self.users:
            user = dict(obj)
            user.update(self.session.get(obj['url']).json())
            self.users[login] = user
        else:
            user = self.users[login]
        # add names for those, that don't have one... TODO: probably should ask about this
        if not 'name' in user or not user['name']:
            if login in github_users_to_names:
                user['name'] = github_users_to_names[login]
                user['_anon_'] = True
            elif 'name' in obj and obj['name']:
                user['name'] = obj['name']
                user['_anon_'] = True
            else:
                user['name'] = login
                if 'github:' + login not in IGNORED_USER_IDS:
                    print(f"    !! warning: no name for: {login} {user['url'], user['html_url']}")

        return {
            'provider': 'github',
            'id': 'github:' + login,
            'name': user['name'],
            'email': user['email'],
            'profile_url': user.get('html_url') if not user.get('_anon_', False) else None,
            'meta': user,
        }

    def contributors(self, project):
        all_users = {}

        url = f'{self.API}/repos/{project}/contributors?anon=true'
        while url:
            print(f" -> {url}")
            r = self.session.get(url)
            data = r.json()
            if isinstance(data, dict):
                raise ValueError(f"API ERROR: {data.get('message') or data}")
            for user in data:
                user = self.get_user(user)
                all_users[user['id']] = user
            next_ = r.links.get('next')
            url = next_['url'] if next_ else None

        return all_users

    def org_repos(self, org):
        # FIXME: if the organisation has over 100 repositories,
        # proper pagination needs to be implemented here so that
        # all repositories are fetched.
        # https://docs.github.com/en/rest/reference/repos#list-organization-repositories
        url = f'{self.API}/orgs/{org}/repos?per_page=100'
        return [repo['full_name'] for repo in self.session.get(url).json()]


gh = Github(token=github_token)
GITHUB_RE = re.compile(r'^\s*\*\s+\[(?P<name>[^]]+)\]\(https://github.com/(?P<project>[^/]+/[^/]+)/\)')


def parse_repositories(path):
    # * [:name](https://github.com/:group/:project/)
    print(f"Parsing repos from {path}")
    repos = []
    with open(path, 'r') as f:
        for line in f:
            match = GITHUB_RE.search(line)
            if match:
                name = match.group('name')
                project = match.group('project')
                print(f"  * {name}: {project}")
                repos.append(('github', project))
    print()
    return repos


def collect_organization_repos():
    repos = []
    print("Collecting repos from organizations...")
    for org in ORGANIZATIONS:
        org_repos = gh.org_repos(org)
        print(f"  * {org}: {len(org_repos)} repos")
        repos += [('github', repo) for repo in org_repos]
    print()
    return repos


def collect_authors(repos):
    print("Resolving authors..")
    authors = {}
    for method, repo in repos:
        project_name = os.path.basename(repo)
        if method == 'github':
            project_authors = gh.contributors(repo)
        print(f"  done {method}:{repo}, with {len(project_authors)} authors")
        for id_, user in project_authors.items():
            if id_ not in authors:
                authors[id_] = user
                user['projects'] = set((project_name,))
            else:
                authors[id_]['projects'].add(project_name)
    print()
    print("Deduplicating and fixing names for authors..")
    all_authors = [user for user in authors.values()
                   if user['email'] not in IGNORED_AUTHORS
                   and user['name'] not in IGNORED_AUTHORS
                   and not any(user['email'] and user['email'].endswith(d) for d in IGNORED_DOMAINS)
                   and user['id'] not in IGNORED_USER_IDS]
    known_users = [user for user in all_authors if user['provider'] is not None]
    email_map = {user['email']: user for user in known_users}
    name_map = {user['name']: user for user in known_users}
    anonymous = [user for user in all_authors if user['provider'] is None]
    for anon in anonymous:
        if anon['email'] in email_map:
            user = email_map[anon['email']]
        elif anon['name'] in name_map:
            user = name_map[anon['name']]
        elif anon['name'] in included_anonymous:
            known_users.append(anon)
        else:
            print(f"  !! warning: ignoring anonymous name: {anon['name']} <{anon['email']}>: {anon['projects']}")
            continue
        user['projects'].update(anon['projects'])
    print()
    return known_users


def print_summary(authors):
    print(f"Authors and projects (total of {len(authors)}):")
    for author in sorted(authors, key=lambda x: (x['name'], x['id'])):
        projects = ', '.join(sorted(author['projects']))
        print(f"  {author['name']}")
        print(f"    {projects}")
        url = author.get('profile_url')
        if url:
            print(f"    {url}")
        else:
            url = author.get('meta', {}).get('html_url')
            if url:
                print(f"    ANON {url}")
    print()


def format_authors(authors):
    lines = []
    for author in sorted(authors, key=lambda x: (x['name'], x['email'], x['id'])):
        profile = author.get('profile_url')
        name = author['name'].strip()
        line = '* '
        if profile:
            line += '['
        if name in REALNAMES:
            line += f"{name} ({REALNAMES[name]})"
        else:
            line += name
        if profile:
            line += f"]({profile})"
        lines.append(line)
    return lines


def partition(lines, first, second):
    first_i = next((i for i, l in enumerate(lines) if l.startswith(first)), None)
    if first_i is None:
        raise ValueError(f"unable to find line starting with '{first}'")
    second_i = next((i for i, l in enumerate(lines[first_i+1:]) if l.startswith(second)), None)
    if second_i is None:
        raise ValueError(f"unable to find line starting wiht '{second}'")
    prefix = lines[:first_i+1]
    suffix = lines[first_i+second_i+1:]
    return (prefix, suffix)


def main():
    filename = 'index.md'
    component_repos = parse_repositories('../../components/index.md')
    organization_repos = collect_organization_repos()
    all_repos = list(set(component_repos + organization_repos))
    all_repos.sort()

    authors = collect_authors(all_repos)
    print_summary(authors)

    with open(filename, 'r+') as f:
        data = f.read().splitlines()
        prefix, suffix = partition(data, '[start-of-contributors]', '[end-of-contributors]')
        # ignore already listed
        contributors = [author for author in authors
                        if not any(author['name'] in line for line in prefix)]
        # update the file
        f.seek(0)
        f.write('\n'.join(prefix))
        f.write('\n\n')
        f.write('\n'.join(format_authors(contributors)))
        f.write('\n\n')
        f.write('\n'.join(suffix))
        f.write('\n')
        f.truncate()

    print(f"File {filename} updated.")

if __name__ == '__main__':
    main()
