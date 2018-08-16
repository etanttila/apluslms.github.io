## Architecture

A-plus is designed to be extendable. The ecosystem includes multiple web
services that communicate with each other. The responsibilities are
divided using interfaces so that the different services and modules
can be individually changed and redesigned.

### Presentations

You can read or use the brief [presentation slide set](/architecture/presentation/),
that was used in Espoo twice in 2018.

### The front

The front module is responsible to

* authenticate learners and educators,
* control learning module access by role and schedule,
* store submission and assessment data,
* create an accessible and effective UI.

The front does not store learning materials but loads everything
from external services via HTTP. Also submissions are posted
to external services that respond with feedback content.

* Software: <https://github.com/Aalto-LeTech/a-plus>
* Protocol description: <https://github.com/Aalto-LeTech/a-plus/blob/master/doc/GRADERS.md>
* Markup reference: <https://github.com/Aalto-LeTech/a-plus/blob/master/doc/CONTENT.md>

In addition to standard A-plus front, a Moodle-plugin exists that
can connect A-plus learning materials as Moodle activities.

* Software: <https://github.com/Aalto-LeTech/moodle-mod_astra>


### The mooc-grader

This is the standard module to provide learning material and automatic
assessment. Each course is read from index configuration that defines
the course material hierarchy and links separate configuration file
for each interactive learning element. The supported features are

* static content (HTML and resources)
* configurable forms to collect input/files (including synchronous assessment)
* asynchronous assessment code execution

Any assessment code can be executed inside custom container environment.
Each assessment executes in new container that is destroyed at end.
The mooc-grader includes a gitmanager module that offers a web
interface to add new courses directly from Git repositories.

* Software: <https://github.com/Aalto-LeTech/mooc-grader>
* Configuration reference: <https://github.com/Aalto-LeTech/mooc-grader/blob/master/courses/README.md>


## Schematics

```

   Student
      |
      | http      _________
      |          |         |                        Staff
A-PLUS-FRONT --->| Records |                          |
      |          |_________|                          |
      | http                                       _______
      |                                           |       |
 MOOC-GRADER <------------------------------------|  Git  |
      |                                           |_______|
      |-- index.yaml                                  |
            |                                         |-- index.yaml
            |-- exercise1.yaml                              |
                  |                                         |-- exercise1.yaml
                  | Docker
                  |
      apluslms/grading-python:3.5

```

```

   Student
      |
      | http      _________
      |          |         |                        Staff
A-PLUS-FRONT --->| Records |                          |
      |          |_________|                          |
      | http                                       _______
      |                               make html   |       |
 MOOC-GRADER <------------------------------------|  Git  |
      |                                           |_______|
      |-- _build/yaml/index.yaml                      |
             |                                        |-- index.rst
             |-- _build/yaml/ex1.yaml                       |
                    |                                       |-- chapter1.rst
                    | Docker
                    |
        apluslms/grading-python:3.5

```
