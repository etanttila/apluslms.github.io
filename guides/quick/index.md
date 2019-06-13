# Quick Start Guide

A+ LMS is complex environment, but this short guide will get you going.
A template course, which also works as full manual, is provided as an A+ course.
This guide will go through the steps to get there.

## Architecture

A+ LMS consists of multiple smaller web services that provide different features for the system.
A+ front or the portal takes care of users and records for them.
Other services typically provide different assessment features or other interactive course material.

This design creates a bit of a challenge as the software is not just a single binary, but it also makes development of features flexible. Check out [the architecture](/architecture/) page for more details.

## Requirements

Currently, we support Linux and macOS.
You can get A+ LMS working on Windows, but it will require some skill and no documentation is provided for that.
Note that you also need administrator privileges (e.g. sudo rights) to install required software.
Furthermore, due to Docker you will have similar permissions as root, so your machine can not be shared with other users.

### Git

Course material, including the template course, is managed using git.
[Git](https://git-scm.com/) is a version-control system or more like a change management tool.
It is used to track changes to the course material and also to update production with a new version.

### Docker

Containers are used in A+ LMS a lot, because they provide sandboxing and an easy method to deliver software images.
To run A+ LMS locally, you need to install [Docker](https://www.docker.com/).
Docker is a containerization software.
Follow [this guide](https://docs.docker.com/install/) to install Docker Community Edition on your machine.
In short, on Linux install `docker-ce` from docker repositories and on macOS download and install Docker for Mac.

### Docker Compose

Currently, we still use docker-compose (version 1.10 or newer) to start local testing environment, so you will need to install it too.
Luckily, docker-compose is part of Docker for Mac, so this is done already in previous step for macOS users.
Starting with Debian Buster and Ubuntu Bionic, you can use docker-compose from the distribution repository, thus you can install it with command `sudo apt install docker-compose` or `aptdcon -i docker-compose`.
With older releases and linuxes, you can follow [this guide](https://docs.docker.com/compose/install/) to install it, but remove sudo and install the binary to your home folder instead.
As of writing, these commands will do it: `mkdir -p ~/.local/bin && curl -L https://github.com/docker/compose/releases/download/1.24.0/docker-compose-Linux-$(uname -m) -o ~/.local/bin/docker-compose && chmod +x ~/.local/bin/docker-compose`.

### Roman

To compile courses, we use [Roman](https://github.com/apluslms/roman).
This is a Python 3 utility, which does run compilation steps in containers (uses Docker installed above).
It replaces `./docker-compose.sh`, which was used in the past.
You can easily install it with command `pip3 install --user apluslms-roman` or use alternative methods documented in [the source repository](https://github.com/apluslms/roman#installation).
**Notice** that Roman requires Python 3 and `pip3` for easy installation.
On Debian/Ubuntu, you can install those with command `sudo apt install python3-pip` or `aptdcon -i python3-pip`.
On macOS, you can install it using [Homebrew](https://brew.sh/) (remember possible security issues) with command `brew install python`.
There are also Python bundled binaries in the Roman github releases page.

### common

Finally, let's add python user installed binaries (and docker-compose on Linux) to the `PATH`.
**Notice** if this step doesn't work for you, you need to adapt it to your local configuration.

```
[ "$(uname -s)" != "Darwin" ] && path_=.local/bin || path_=Library/Python/$(python3 --version|cut -d' ' -f2|cut -d. -f1-2)/bin
echo "export PATH=\${HOME}/$path_\${PATH:+:}\${PATH:-}" >> ~/.profile
```

**You need to logout and login again for this change to take effect (typically).**

_For the interested, the linux path is documented on [freedesktop site](https://www.freedesktop.org/software/systemd/man/file-hierarchy.html#Home%20Directory)._

### Summary

To summarize, you need these tools:

* Linux or macOS
* git
* docker-ce (Docker Community Edition, Docker for Mac)
* docker-compose 1.10+ (included in Docker for Mac)
* `roman` (apluslms_roman) from PyPi
  * Python 3.5+ (`python3-pip` or via Homebrew on macOS)
  * or Roman binary with bundled Python

## Start your first course

First, download a copy of [the course manual](https://github.com/apluslms/course-templates/), it will work as your template.
Open terminal and move to a folder where you want to store your courses.
Then execute `git clone https://github.com/apluslms/course-templates.git my_new_course`.
Move in the course folder `cd my_new_course`.

Second, update git submodules as RST extensions are still distributed this way.
So, execute `git submodule init && git submodule update`.

We now have the course material in correct place and it's ready for compilation.
We store only the source material in git repository and final presentation and configuration files are build on your machine for local developing and on the server for production.
So, compile course material with command `./docker-compile.sh`.

Now everything is ready for running the manual course.
Start A+ LMS with command `./docker-up.sh`.
You will see a lot of log messages from few containers and after a while there won't be any new messages.
A+ LMS is now running.

To stop A+ LMS, press Q, S, ESC or CTRL+C in the terminal.
S and ESC will keep the database and other files, while Q and CTRL+C will remove all data assosiated with running the system.
For rapidly testing parts of your course, you can press S or ESC to stop A+ and then restart with the same data.
Time to time, it's good to remove the data, so all the test submissions are cleaned for example.

You now open <http://localhost:8000> and you should see A+ front page.
Open the course and read more.
Test environment has three users: _root_, _assistant_ and _student_.
Password for every user is the same as the user name.

To summarize, execute the following:

```
git clone https://github.com/apluslms/course-templates.git my_new_course
cd my_new_course
roman build
./docker-up.sh
```

## Troubles?

* Ports: you can't have anything in ports `8000`, `8080` or `3000` as they are used by A+ LMS.
