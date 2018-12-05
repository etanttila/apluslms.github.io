# Components

Only a few services are [core](#core) components for any A+ LMS installation.
[Common](#common) components listed here are often found from well featured installations,
but they vary depending on needs of the organization.
Lastly, there are some commonly used [utilities](#utilities), which are separate from A+, but often used with it.

Remember that this is not a complete list and organizations have custom assessment services and tools for particular needs.

## Core

These components are the corner stones of any A+ LMS installation.
The [release schedule](/releases/#release-schedule) applies to these.

* [A+ portal](https://github.com/aalto-letech/a-plus/)

  The user facing web portal.
  Contains course definitions, retrieves course material and exercises, presents them to the user and records points and grades.
  Basically, it's the user interface and the data storage.

  It's possible to have similar, but limited, features in a moodle using a plugin [mod_atra](https://github.com/Aalto-LeTech/moodle-mod_astra/).

* [MOOC Grader](https://github.com/aalto-letech/mooc-grader/)

  An automatic assessment framework.
  Can provide multiple different exercise types including questionnaires and programming exercises.
  Can run assessment code provided by course staff in docker containers.
  This enables diverse possibilities including assessment of a small python program or an android application for example.

  Currently, this service also handles course building and configuration for itself and A+ portal.

* [a-plus-rst-tools](https://github.com/aalto-letech/a-plus-rst-tools)

  Set of Sphinx extensions for creating interactive course material with RST.

## Common

Some commonly used assessment and support services.

* [MOOC Jutut](https://github.com/aalto-letech/mooc-jutut/)

  An interactive feedback or learning journal service.
  Presents a form for students to fill their thoughts or problems,
  which are then accepted or answered by the course staff.

* [Radar](https://github.com/aalto-letech/radar/)

  Automatic similarity analysis for source code and other tokenizable data.
  Can be used to observe patterns in student submissions.
  Furthermore, can even be used to find possible cases of plagiarism,
  though always do a thorough manual validation for every case.

* [Rubyric](https://github.com/aalto-letech/rubyric/)

  Rubric-based assessment tool.
  A service that provides manual grading for file submission with an assessment guide.
  Works well for project reports and manually graded project files.

## Utilities

Utility services that are often helpful.

* [Neuvontajono](https://github.com/ttsirkia/neuvontajono/)

  Neuvontajono is an interactive queue system for lab sessions (neuvontajono in Finnish) where students can ask help from course assistants.
  Students see their position in the queue and assistants see the students in the queue, both in real time.
  This provides a bit more fair allocation of assistant time per student.
  Includes information about waiting times and queue lengths per a session for the teacher.

* [Koodisäilö](https://github.com/ttsirkia/koodisailo/)

  This app implements kind of a Pastebin service.
  A student can store code snippets in the service so they can work with them in other location or so they can share it with the course staff.
  Code snippets are not visible to other users, except to the course staff if direct link is provided.
  Thus, a student can safely share the link in a forum or a chat without other students seeing the content.
