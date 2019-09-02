:title: Cloud+LMS
:author: Jaakko Kantojärvi
:description: Cloud First Learning Management Systems

:data-transition-duration: 1000

:css: presentation.css

.. header::

   .. image:: https://apluslms.github.io/assets/images/apluslogo.png

.. footer::

   Cloud+LMS | Jaakko Kantojärvi

   .. image:: aalto.png

----

:data-scale: 1
:data-x: r1200
:class: center_text

Cloud First Learning Management Systems
=======================================

|

Jaakko Kantojärvi

A+ lead developer & DevOps


----

:class: always

Expectations from modern LMSes
==============================

|

----

:data-x: r0
:data-y: r200

* Interactive online material (book, workbook, course)
* Automatically graded exercises
* Instant feedback
* Peer review (and maybe grading)

.. note::

    1 / 7

    * online
    * exercises
    * feedback
    * peer

----

:data-y: r25

* Personalisation, problem randomisation, exercise pools
* Online editors, code testing, highlighting
* Plagiarism, student action tracking
* Analytics, tracking of learning patterns

.. note::

    2 / 7

    * personalisation
    * editors
    * plagiarism
    * analytics

----

* Export and import user data
* Security and secrecy
* Forgetting personal data
* Interconnections to other systems

.. note::

    3 / 7

    * export
    * security
    * forgetting
    * connections

----

* Extendability, add-ons and extensions
* Existing interfaces: LTI, H5P
* Customisation: teachers own code
* Authenticity of students actions

.. note::

    4 / 7

    * extendable
    * existing stuff
    * customisation
    * authenticity

----

* Massive online courses
* Responsiveness, scaling
* Robustness, no downtimes!
* Automatic grades and updates to SISU

.. note::

    5 / 7

    * MOOC
    * responsiveness
    * robustness
    * automatic grades

----

* Course material production
* Shared materials, cooperation and co-authoring
* Exercise sharing and catalogs
* Course release management

.. note::

    6 / 7

    * production
    * shared stuff
    * course releases

----

* IT operations are easy: software upgrades, deployment
* All the stuff we don't care about...
* All the stuff I don't know about...

.. note::

    7 / 7

    * IT operations

----

:data-y: r400
:class: center_text

Lot of challenges
=================

So how do we can make a software to solve all of these needs?

----

:data-rotate: r90
:data-x: r800
:data-y: r800

1. **Platform to provide robustness and scale**
2. Software design to support scale and extensibility
3. DevOps to course material production
4. Tools and automation to support IT operations

----

:data-rotate: r0
:data-y: r2000
:data-x: r0
:class: always

Short history of platforms
==========================

----

:data-y: r0
:data-x: r-300

Bare-metal:

* good: dedicated resources, speed, easy to understand and operate
* bad: maintenance, no redundancy, power outages, requires knowledge, vertical scaling has a limit

----

:data-x: r-50

Virtual machines:

* good: maintenance is better than with bare-metal,
  can be migrated online, backups,
  easy to deploy multiple versions
* bad: where developer ends and IT operator starts,
  requires lot of system administration (software upgrades, Ansible, Puppet),
  scaling is often done manually

----

Containers:

* good: developer provides full OS environment with the app,
  service components (Web, DB, FS) can split to different containers,
  scaling can often be automatic
* bad: managing the complexity is hard,
  security updates to environment,
  git clone + django migrate is not enough!

----

:data-x: r-600

Brief history..
===============

* Unix V7 introduced ``chroot`` in 1979 (`article <https://blog.aquasec.com/a-brief-history-of-containers-from-1970s-chroot-to-docker-2016>`_)

* Solaris Containers released in Solaris 10, 2004

* *"Starting in Linux 3.8 (Feb 18, 2013), unprivileged processes can create user namespaces,
  which opens up a raft of interesting new possibilities for applications"*
  (`lwn.net <https://lwn.net/Articles/531114/>`_)

* Docker was released 23 days later on March 13, 2013

----

.. raw:: html

  <script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/1845_RC03/embed_loader.js"></script>
  <script type="text/javascript"> trends.embed.renderExploreWidget("TIMESERIES", {"comparisonItem":[{"keyword":"docker","geo":"US","time":"2006-01-01 2019-08-20"},{"keyword":"kubernetes","geo":"US","time":"2006-01-01 2019-08-20"},{"keyword":"vmware","geo":"US","time":"2006-01-01 2019-08-20"}],"category":0,"property":""}, {"exploreQuery":"date=2006-01-01%202019-08-20&geo=US&q=docker,kubernetes,vmware","guestPath":"https://trends.google.com:443/trends/embed/"}); </script>

----

Kubernetes
==========

* Container orchestration
* Automating deployment and scaling
* Abstracts computing and storage resources
* Developer provides application as an OS image
* IT operations provide resources
* Supported by many cloud platform providers

----

Private cloud for teaching
==========================

* Information security
* Some level of secrecy required for student solutions
* Ensures low latencies
* Requires a good DevOps skills from IT team

----

CS Kubernetes
=============

Provides MOOC-Grader and Jupyter Hub for CS

* 3x schedulers: 4-32 CPU, 4-128 GB RAM
* 2x workers: 32 CPU, 128GB RAM
* 2x workers: 16 CPU, 64 GB RAM

----

* Containers solve scaling..
* But require somewhat microservice design from the application



----



:data-y: r-2000
:data-x: r0

1. Platform to provide robustness and scale
2. **Software design to support scale and extensibility**
3. DevOps to course material production
4. Tools and automation to support IT operations

----

:data-y: r2000
:data-x: r0

It was easy..
=============

* Desktop apps are simple problem, download and run
* Django apps are also simple, ``git clone && ./manage.py runserver``
* A lot of users
  → add more cores and RAM

----

:data-y: r0
:data-x: r-600

What if there is 10k users, 100k or 1M?
=======================================

¯\\_(ツ)_/¯
-----------

----

Scalability from microservices
==============================

* Containers are light-weight "virtual machines"
  → ideal for microservices
* Interfaces between components
  → high availability per component
  → robustness
* Automatic scaling per component
  → identify problematic components

----

Distribute development
======================

* Implement features as services
  → extensibility due common interfaces
* Separate teams can work on different components
* Separation requires problem handling and testing
  → robustness and better software!
* Failed separation results in a house of cards
  → problem in one service brings everything down

----

Downsides..
===========

* "What is part of a release?"
* "How do I install this?"
* "Feature X doesn't work on my machine."
* "We would need 10 virtual machines to set this up"



----



:data-y: r-2000
:data-x: r0

1. Platform to provide robustness and scale
2. Software design to support scale and extensibility
3. **DevOps to course material production**
4. Tools and automation to support IT operations

----

:data-y: r2000
:data-x: r0

DevOps
======

* Closes the cap between development and IT operations
* Continuous Integration, i.e. git + automated tests
* Continuous Deployment, i.e. update production on a release push
* Supports agile software development, containers and microservices

----

:data-y: r0
:data-x: r-600

Digitalisation in teaching
==========================

* First, teachers wrote material with latex and exported pdf.
  Nice documents for the student to read offline.
  No interactive elements.

* Then, they clicked in moodle and wrote text boxes.
  Interactive elements!
  Often a single release and no rollbacks.

----

DevOps for teaching
===================

* Course material written in some source format
* ... or use WYSIWYG editor for it
* Text and exercises from different people
* Push material to version control for a release
* Integration tests begin → "Did I break exercises?"
* Automated deployment to test and production environments!

----

Why?
====

* Ensure material in production is not broken
* Create multiple releases: eBook vs. course
* Deploy to multiple platforms: A+, TIM, ACOS
* Hide microservice design from the teacher
* Material cooperation between authors



----



:data-y: r-2000
:data-x: r0

1. Platform to provide robustness and scale
2. Software design to support scale and extensibility
3. DevOps to course material production
4. **Tools and automation to support IT operations**


----


:data-y: r2000
:data-x: r0

Industry tools
==============

* Release services via image repositories: `Docker Hub <https://hub.docker.com>`_, `Google Container Registry <https://gcr.io>`_
* Software definitions as Helm charts: `helm.sh <https://helm.sh>`_
* Cluster deployment using Helmsman: `github <https://github.com/Praqma/helmsman>`_


----

:data-y: r0
:data-x: r-600

Separation of roles
===================

* Developer produces the software and defines execution environment
* IT operations ensures computing and storage resources
* No need for ops to develop or devs to operate
* Except all the DevOps building all the images 😁


----

:data-rotate: r-90
:data-y: r-600
:data-x: r-600

Vision for the future
=====================

* no need to care about platform used by students
* material can be distributed via multiple platforms
* teacher creates only part of the material
* availability of interactive elements and exercises
* teacher has visibility over what is working

----

:data-rotate: r0
:data-x: r0
:data-y: r200

Teacher has time to provide best of the world learning experience,
as the tools are so awesome!

|

Teacher has analytics and feedback to make it event better!

----

IT operators can maintain 99.9% service level!

|

Students are happy as they can read to exams..

----

We do not implement same features over and over again...

----

:data-x: r1200
:data-y: r0

Underway
========

* Roman - define how material is build (i.e. Makefile)
* Shepherd - CI/CD tool for teaching (i.e. easy to use Gitlab CI / drone.io)
* helmsman and deployment tools for IT

----

:data-x: r0
:data-y: r200

To plan
=======

* ACOS as an exercise catalog and a proxy
* distributed container grader (i.e. MOOC-Grader v2)
* A+ v2

----

:data-rotate: r360
:data-x: r0
:data-y: r0

:class: center_text

Questions?
==========

More info on

`apluslms.github.io <https://apluslms.github.io>`_
