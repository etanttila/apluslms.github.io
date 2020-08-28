# GNU Gettext Translations

The goal with following rules is to lower amount of problems when working with git.
Idea is not to update fields that do not add any value and fields that are not relevant for the change in a commit.

* Only `.po` files to git, i.e., no `.mo` files.

  * The `.mo` files should be compiled by the packaging system and locally during development.

* If no reason not to, use English string as message id (i.e. default string) and make translations for other languages (e.g. Finnish).
* Use translation tool, they format the file correctly.
  Or run a script which merges the `.po` files, which reformatting.
* Do not add line numbers, but add filenames, as it makes simple changes in the git.
  This can be done with the `--add-location=file` option in most gettext tools.
* No need to set or update meta headers at the top of a `.po` file, as those details are typically available from the git.
  However, if the translation was done by a non-git user, then those fields could be used.
  It's recommended to write those details in the commit message too (e.g., add the `Co-Authored-By` header).
* No need to keep obsolete translation strings, as they are in the git history.


## Django specific stuff

* Use `trimmed` in `blocktrans`
* Typical `makemessages` call:

  ```sh
./manage.py makemessages --ignore='venv*/*' --no-obsolete --add-location file
```
