:title: Future and roadmap of A+ LMS
:author: Jaakko Kantojärvi
:description: Short presentation about future and current roadmap of A+ LMS and it's microservices

:data-transition-duration: 2000
:skip-help: true

:css: presentation.css

.. header::

   .. image:: https://apluslms.github.io/assets/images/apluslogo.png

.. footer::

   Future and roadmap of A+ LMS by Jaakko Kantojärvi

   .. image:: aalto.png


----

:data-y: r-1200
:data-x: 0
:class: center_text

Future visions and roadmap for A+ LMS
=====================================

… after 6 years of prototyping.


----

:data-y: 0
:data-x: 0

Design principles
=================

* One service should do one thing well.
* Make services error resilient. No cascading failures.
* Refactor and redesign. Pay back technical dept.
* From prototypes to real mature products.
* Utilize containers.

.. note::

   One service, one purpose
    * No big monolithic services, which can't be updated piece by piece
    * Supports distributed development
    * Can be taken to use one some courses first

   Error handling
    * Service can't get stuck, return errors or break when another service is broken
    * Stop cascading errors

   Technical dept (Tekninen velka)
    * Mature all core services
    * Prototyped features have created it

   Containers
    * Provide nearly platform independent method for software delivery
    * Security via sandbox
    * Code from teachers is also untrusted for the system


----

:data-x: r1200

Why containers?
===============

* Teacher can specify the software environment.
* Kind of platform independent. We can support Linux, macOS and Windows at least.
* Security. An untrusted code is executed within a sandbox.

.. note::

   Environment
    * Image can contain nearly any kind of software environment
    * Teacher can provide their own image

   Availability
    * Image can be run on a computer of anyone (any other teacher)
    * Image is the same on both, teacher's machine and on the server.

   Security
    * Teacher's code is untrusted for other teachers and for the system
    * Containers provide sandbox, so we can run untrusted code


----

Outline for changes
===================

* Split features to dedicated services

  * Course edit from A+ and gitmanager from grader
  * Own services for grader questionnaires, container exerces and CDN roles

* From scripts and hacks to software.

  * Remove :code:`docker-compile.sh` and :code:`docker-up.sh`
  * No scripts/modules in course repositories

.. note::

   Move
    * course edit interface from A+
    * gitmanager from grader
    * cdn
    * questionnaires
    * container exercises

   Scripts -> Software


----

:data-y: r1200
:data-x: r0
:class: center_text

New components
==============


----

:data-y: r0
:data-x: r1200

Roman library
=============

* Generic course material build process (like make).
* Not specific to A+, could be used for anything.
* Unify building between a local machine and the server.
* Compile from source (git) to presentation (html).
* Collect configuration information for different services

.. note::

   * Course material is source and compilation provides presentation
   * Generic tool. Can be used to build anything where containers are build tasks
   * Predefined environments (containers) so identical build always on all systems
   * Git shouldn't contain build results
   * Build should create indentical result every time
   * Collect information (config and data) for different ervices


----

Roman GUI
=========

* No need to understand terminal
* Requires less knowledge about computers
* Possible to support windows
* Build material, start local test environment, upload material to production

----

.. https://www.youtube.com/watch?v=Z87cAYNNtWQ

.. raw:: html

  <div id="ytplayer"></div>
  <br><button id="ytplay">Play fullscreen</button>
  <script>
    var tag = document.createElement('script');
    tag.src = "https://www.youtube.com/player_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    function onYouTubePlayerAPIReady() {
      var player = new YT.Player('ytplayer', {
        videoId: 'Z87cAYNNtWQ',
        height: '360', width: '640', disablekb: 1, suggestedQuality: 'hd720',
        events: { 'onStateChange': onStateChange, },
      });
      document.getElementById('ytplay').addEventListener('click', function(event) {
        var iframe = player.getIframe();
        var requestFullScreen = iframe.requestFullScreen || iframe.mozRequestFullScreen || iframe.webkitRequestFullScreen;
        if (requestFullScreen) requestFullScreen.bind(iframe)();
        player.playVideo();
        player.setPlaybackQuality('hd720');
      });
      function onStateChange(event) {
        if (event.data == YT.PlayerState.ENDED) {
          var exitFullscreen = document.exitFullscreen || document.mozExitFullscreen || document.webkitExitFullscreen;
          if (exitFullscreen) exitFullscreen.bind(document)();
        }
      }
    }
  </script>


----

Course management service
=========================

* One service does one thing well
* Cloud management: manage other parts of the LMS
* Move here all course management from A+
* Configures production and testing environments
* In future, could support multiple learning management systems, e.g. Moodle
* Possible names: godfather, godmother, shepherd

.. note::

   Names
    * original prject name: godfather
    * not very neutral for everyone
    * shepherd has similar meaning, but no relation to gender etc.

   Course management
    * Move all administration interfaces here
    * Configures other services (e.g. A+) over web API
    * Can support multiple environments: testing vs. production

   Other LMS:
    * Could support updates to mycourses or opendsa for example


----

Container grader v2
===================

* Dedicated for container exercises
* Assessment queues and priorities
* Track task progress (completion)
* Interfaces for non-graded tasks
* Don't expect A+ to be alive

.. note::

   Dedicated
    * One service does one thing well
    * Move questionnaires to another service (grader v1 for now, later a new service)
    * Move ajax stuff to another service

   Queues
    * Slow and fast queues for bigger and smaller tasks.
    * Task completion speeds, queue lengths and time estimates

   Puppet
    * From fire and forget to managed task running
    * Keep track of started tasks, record feedback
    * Record feedback and clean task from db when delivered to record storage (A+)


----

RST toolchain v2
================

* Move from submodule to docker container
* From sphinx extensions to software (Ariel)
* Design for the future
* Clean and generalize directives
* Unify directives and remove duplicates
* Extendable and modular system

.. note::

   * Submodules have problems. Track versions with container tags
   * Create software, Ariel, with support for extensions
   * Design so future updates work well and minimize upcoming breaking changes
   * Rewrite RST directives or at least check all of them
   * Remove conf.py and use cleaner (yaml) interface. support for advanced sphinx hacks of course


----

:data-y: r1200
:data-x: r0
:class: center_text

When?
=====


----

:data-y: r0
:data-x: r1200

Releases
========

* Two main release windows per year.
* August: A summer release & January: A winter release
* Feature freeze two months before: June & November
* Next: liekovarpio, January 2019

 * A+ v1.4, MOOC-Grader v1.4
 * The feature freeze in few weeks.


.. note::

   Two releaes
    * August (Elokuu) summer release (freeze in June (Kesäkuu))
    * January (Tammikuu) winter release (freeze in November (Marraskuu))

   Next releaes
    * liekovarpio, January. v1.4 of tools


----

2019
====

January - liekovarpio:

* Roman used for local building
* GDPR updates

August:

* Management service prototype
* Roman used in management service
* Grader v2 with some courses


----

2020
====

January:

* Management service replaces gitmanager
* Grader v2 for all container exercises
* mood-grader for questionnaires etc

August:

* Ariel, RST v2
* Roman replaces :code:`docker-up.sh`
* Roman GUI prototype


----

2021 ->
=======

* Roman on windows
* Windows course development and testing supported
* A+ v2 design
* A+ v2 prototype


----

:data-y: r1200
:data-x: r0
:class: center_text

|
|

Questions?
==========

More info on

`apluslms.github.io <https://apluslms.github.io>`_
