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
Furthermore, due to Docker you will have similar permissions any case, so there can not be other users on your machine.

Course material, including the template course, is managed using git.
[Git](https://git-scm.com/) is a version-control system or more a change management tool. It is used to track changes to the course material and then to update production with a new version.

Containers are used in A+ LMS a lot, because they provide sandoxing and an easy method to deliver software images.
To run A+ LMS locally, you will need to install [Docker](https://www.docker.com/), a containerization software.
Follow [this guide](https://docs.docker.com/install/) to install Docker Community Edition on your machine.
In short, on Linux install `docker-ce` from docker repositories and on macOS download and install Docker for Mac.

Currently, we still use docker-compose to start local testing environment, so you will need to install it too.
Follow [this guide](https://docs.docker.com/compose/install/) to install it.
Note that you can use path `$HOME/.local/bin` to store the script as long as you add it to your _PATH_.

To summarize, you need these tools:

* Linux or macOS
* git
* docker community edition (docker-ce)
* docker-compose

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
git submodule init
git submodule update
./docker-compile.sh
./docker-up.sh
```

## Troubles?

* Ports: you can't have anything in ports `8000`, `8080` or `3000` as they are used by A+ LMS.
