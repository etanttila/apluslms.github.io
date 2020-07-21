# Protocols

Protocol definitions are import for service-oriented architecture.
Major protocols used by [components](../components/) of the A+ LMS are listed here.
Some of the protocols are created by the project and have documentation here.
For the rest, links are provided to respective documentations.
Additionally, links to machine readable definitions (e.g. [gRPC](https://grpc.io/) files) are provided when available.


## Content service interfaces

Protocols to retrieve and manage course or other study material.
These protocols are between the client (tool used to read the material) or the LMS and the service providing the content.

* [A+ Material v1](aplus-material-v1)
  is a simple protocol to retrieve course material and definition how to mark exercises in the document.


## Assessment service interfaces

Protocols for the LMS to retrieve exercises and to request assessments for submissions.

* [A+ Assess v1](aplus-assess-v1/)
  is a simple HTTP based protocol.
  It supports both synchronous and asynchronous assessment.

* [LTI 1.1](http://www.imsglobal.org/specs/ltiv1p1/implementation-guide)
  is a global standard to connect tool providers (i.e. assessment services) to a tool consumer (i.e. the LMS).
  It supports opening a tool in a sandbox (iframe or new window) and pushing grades back to the LMS.
  However, it does not support storing student solutions in the LMS for staff review or debugging.


## Assessment presentation formats

Protocols to support formatting exercise definitions and feedback.

* [Bootstrap 3](https://getbootstrap.com/docs/3.3/)
  is a popular framework for styling web pages.
  The Bootstrap 3 CSS rules should be valid inside an exercise, when it has `class="exercise-with-bootstrap3"`.

* [A+ Quiz v1](aplus-quiz-v1/)
  is a set of CSS classes to help style questionnaire forms.
  These CSS rules should be valid inside an exercise, when it has `class="aplus-quiz1"`.


## Browser interface for interactive exercises

Protocols in the web view of the LMS.

* [A+ JavaScript v1](aplus-js-v1/) (DRAFT)
  is a simple [CustomEvent](https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent) based interface to interact with the process of embedding exercises to the material.


## Webhooks

A webhook is web requests made when a specific events occur.
The request contains data about the event.
These enable creating a reactive network of services.

* [A+ Hook v1](aplus-hook-v1)
  is a simple hook provided by the A+ LMS.
  It will be triggered when assessment completes.
