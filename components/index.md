# Components

Only a few services are [core](#core) components for any A+ LMS installation.
[Common](#common) components listed here are often found from well featured installations,
but they vary depending on needs of the organization.
Lastly, there are some commonly used [utilities](#utilities), which are separate from A+, but often used with it.

Remember that this is not a complete list and organizations have custom assessment services and tools for particular needs.

## Core

These components are the corner stones of any A+ LMS installation.
The [release schedule](/releases/#release-schedule) applies to these.

* [A+ portal](https://github.com/apluslms/a-plus/)

  The user facing web portal.
  Contains course definitions, retrieves course material and exercises, presents them to the user and records points and grades.
  Basically, it's the user interface and the data storage.

  It's possible to have similar, but limited, features in Moodle using the plugin [mod_astra](https://github.com/Aalto-LeTech/moodle-mod_astra/).

* [MOOC Grader](https://github.com/apluslms/mooc-grader/)

  An automatic assessment framework.
  Can provide multiple different exercise types including questionnaires and programming exercises.
  Can run assessment code provided by course staff in docker containers.
  This enables diverse possibilities including assessment of a small python program or an android application for example.

  Currently, this service also handles course building and configuration for itself and A+ portal.

* [a-plus-rst-tools](https://github.com/aalto-letech/a-plus-rst-tools/)

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

* [Acos server](https://github.com/acos-server/acos-server)

  Browser-based smart learning content in a reusable and interoperable way.
  The core idea is that different types of smart learning content can be
  hosted in Acos and offered to various Learning Management Systems (LMS)
  using different protocols.

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

* [Peer-review platform](https://github.com/piehei/prplatform/)

  Students peer-review each other's submissions.
  This tool can be used standalone or with A+ using LTI integration.

* [Grading helper](https://github.com/eliisav/gradinghelper)

  Tool for teachers for managing the process of manual assessment of student projects.
  Teachers allocate students to certain teaching assistants:
  one student is allocated to one teaching assistant for the supervision and
  assessment of the project.
  Teaching assistants report on their assessment progress:
  the tool can track different stages of the assessment work until it is finished, and
  which students have been completely assessed and which are unfinished.

* LaRST (LaTeX-to-RST) (the project repository is not yet publicly available)

  Tool for compiling course materials defined in LaTeX into the RST format of a-plus-rst-tools.
  This allows teachers to write A+ course contents in LaTeX without RST.
