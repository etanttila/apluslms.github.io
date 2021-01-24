:title: Architecture of A+ LMS
:author: Jaakko Kantojärvi
:description: Short presentation about high level architecture of A+ LMS and it's microservices

:data-transition-duration: 2000
:skip-help: true

:css: presentation.css

.. header::

   .. image:: https://apluslms.github.io/assets/images/apluslogo.png

.. footer::

   Architecture of A+ LMS by Jaakko Kantojärvi

   .. image:: aalto.png

----

:data-scale: 1
:data-x: r1200

Architecture of A+ LMS
======================

Flexibility from microservices
------------------------------

----

What is A+ LMS?
===============

A+ is a learning management system.

* Online course material
* Automatic assessment for exercises
* Interactive learning elements
* Exercise point management per student

.. note::

    * features of any LMS

----

Why A+ when there is other systems?
===================================

* Can safely evaluate code from students
* Student groups created by students themselfs
* Good course material workflow
* Flexible and extendable architecture
* Easy to create new assestment tools
* Easy to connect new external services


----

:data-scale: 4
:data-x: 8000
:data-y: 0
:class: always

Microservices
=============

.. image:: design.svg
   :class: design

----

:data-scale: 4
:data-x: 8000
:data-y: 2500
:data-rotate-x: -30
:data-rotate-y: 0
:data-rotate: 0

Why multiple services?
======================

* Each service does one thing well
* Makes system flexible
* Using existing parts is simple
* One course doesn't break others
* Custom tools for single course

----


:data-scale: 1
:data-x: 8000
:data-y: 1300
:data-rotate-x: -20
:data-rotate-y: 0
:data-rotate: 0

A+: the student interface
=========================

* User authentication via University IdP or Google
* Does access control (student, assistant, teacher)
* Bookkeeping: exercise points and grade
* Notifications

.. note::

   * handles auth
   * access control: student, assistant, teacher
   * bookkeeping: points, submissions
   * notifications: exercise is graded, feedback from staff

----

:data-x: 8330
:data-y: 120
:data-rotate-x: -20

Learning content
================

* Text material (html & css)
* Exercise (html form / javascript)
* Retrieved from other services
* Represented as part of A+

.. note::

   * A+ doesn't care where the content comes from
   * Content is served via A+
   * anything that is HTML / CSS / javascript
   * submissions tracked by A+


----

:data-x: 7350
:data-y: 250
:data-rotate-x: -15
:data-rotate-y: -15
:data-rotate: 40

Exercise assessment
===================

* Simple html post and response
* Synchronous assessment (questionnaires)
* Asynchronous assessment (programming exercises)
* Assessment grade is recorded into A+

.. note::

   * Simple protocol
   * Easy to create custom grading service

----

:data-x: 7100
:data-y: 50
:data-rotate-x: -20
:data-rotate-y: -10
:data-rotate: 30

MOOC-Grader
===========

* Safe way to evaluate student code
* Environment defined with Docker images
* Processing pool handled by Kubernetes
* Assessment request from A+
* Asynchronous response when evaluation is completed

----

:data-x: 9850
:data-y: 0
:data-rotate-x: -20
:data-rotate-y: 10
:data-rotate: -10

Other assessment services
=========================

* ACOS - interactive exercises to multiple LMSes
* Rubyric - report assessment, peer review
* MOOC-Jutut - interactive feedbacks
* Radar - plagiarism checking (for code)
* Create more with simple http+form protocol!

----

:data-x: 9800
:data-y: 1000
:data-rotate-x: -20
:data-rotate-y: 10
:data-rotate: -10

External & Utility services
===========================

* Piazza - Discussion forum
* Code paste - Tool for students to share snippets
* Assist queue - Fair assistant time use
* Easy to create or connect more services

----

:data-x: 7300
:data-y: 1390
:data-rotate-x: -20
:data-rotate-y: 0
:data-rotate: 0

Material authoring
==================

* Write material in Ariel (reStructuredText)
* *or with something else*
* Compile material to html and yaml with Roman
* Write unit tests for programming exercises

.. note::

	* ariel - formelly known as a-plus-rst-tools

----

:data-x: 6600
:data-y: 1390
:data-rotate-x: -20

Test on your machine
====================

* Test early and break things before production
* Develop docker image to work with your exercises
* Rapid development

----

:data-x: 6200
:data-y: 700
:data-rotate-x: -20

Push for production
===================

* Manage changes with git
* Push changes to staging
* Push working version to production

----

:data-x: 7400
:data-y: 450
:data-rotate-x: -20
:data-rotate-y: -8
:data-rotate: 15

Automatic update
================

A+ and other services are automatically updated

----

:data-x: 6400
:data-y: 300
:data-rotate-x: -20
:data-rotate-y: -5
:data-rotate: 10

Share material
==============

* Use gitlab/github/etc to share material
* Collaborate with other Universities
* Teacher writes material
* Assistant creates exercise unit tests

----

:data-x: 6000
:data-y: 400

A lot of existing work!
=======================

Ohjelmointi 1 & 2, Studio 2

  Scala exercises

  Animated storytelling

  JSVEE code animations

  Example code annotations

  Questionnaires with specific hints

  Git tutorial (Studio 2)

Ohjelmoinnin peruskurssi Y1 & Y2

  Python exercise

  UML modelling (Y2)

----

:data-x: r-100
:data-y: r400

A lot of existing work!
=======================

Data Structures and Algorithms Y & S.

  JSAV visual algorithm exercises

Databases

  Relational algebra

  SQL queries

Tietotekniikka sovelluksissa

  Numpy, Matlab, LabVIEW, SQL, HTML

----

A lot of existing work!
=======================

Mobile Cloud Computing

  Assess Android software with a virtual screen

Web Software Development

  Assess web code using virtual web browser automation

  Exercises submitted as git repository

*Nearly anything is possible with containers!*


----

:data-scale: 2
:data-x: 7960
:data-y: 1700
:data-rotate-x: -40
:data-rotate-y: 0
:data-rotate: 0
:class: center_text

.. image:: mycourses.svg
   :class: mycourses

Interoperability
================

* Microservices are reusable with other LMSes

* For moodle, there is `mod_astra <https://github.com/apluslms/moodle-mod_astra>`_. with implementation for core A+ features.

----

..

	:data-scale: 2
	:data-x: 8000
	:data-y: 1400
	:data-rotate-x: -40
	:data-rotate-y: 0
	:data-rotate: 0
	:class: center_text

:data-scale: 4
:data-x: 8000
:data-y: 1300
:data-rotate-x: 0
:data-rotate-y: 0
:data-rotate: 0
:class: center_text

|
|

Questions?
==========

More info on

`apluslms.github.io <https://apluslms.github.io>`_
