# A+ JavaScript interface version 1 (DRAFT)

This interface documents how a custom JavaScript code (provided as a plugin, by the content service, or by the assessment service) may hook into the exercise embedding process.
The interface can be used to implemented custom exercise types or to replace the exercise embedding process.

**N.B.** This protocol is still a draft and is based on the current implementation in the A+ portal.


## The Event Interface

The interface is based on the [CustomEvent](https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent) API.
Here is a list of all the events part of the interface:

* `aplus:chapter-loaded`
  is send from the chapter element after it has been loaded.

* `aplus:chapter-ready`
  is send from the chapter element after all exercises have been loaded.

* `aplus:exercise-loaded` with data `{type: exercise_type}`
  is send from the exercise element after the exercise has been downloaded.

  _to be designed_:
  - Define that `event.preventDefault()` can be used to disable the default exercise process (i.e. so that the LMS does not add exercise frame and so on).
    This will disable the `aplus:exercise-ready` event for this exercise.

* `aplus:exercise-ready` with data `{type: exercise_type}`
  is send from the exercise element after the exercise binding has completed, i.e., all event listeners for the `aplus:exercise-loaded` and the default action has completed.

* `aplus:submission-aborted` with data `{type: exercise_type}`
  is send from the exercise element when the submission is aborted before ajax request.

  _to be designed_:
  - Add the submission data to the event data.

* `aplus:exercise-submission-failure` with data `{type: exercise_type}`
  is send from the exercise element when the submission has failed during the ajax request.

  _to be designed_:
  - Rename this to `aplus:submission-failed` to match names of other events.
  - Add the submission data to the event data.
  - Add the ajax failure reason (e.g. network problem, invalid data, and so on) to the event data.

* `aplus:submission-finished` with data `{type: exercise_type}`
  is send from the exercise element when the submission was successfully send.
  If the submission trigger reload, then the process repeats and `aplus:exercise-loaded` etc. are send again.


The list of exercise types, which may be part of the `exericse_type` field:

* `text/x.aplus-exercise` - normal A+ exercise
* `text/x.aplus-exercise.quiz.v1` - core A+ questionnaire type
* `text/x.aplus-exercise.iframe.v1` - core A+ iframe type
* `text/x.aplus-exercise.active-element.v1` - core A+ active-element type


## The postMessage API

The older interface is based on `window.postMessage` API.
However, this interfaces is not as flexible as the Event API, hence all new code should use the Event API instead.

* `{type: 'a-plus-refresh-stats'}`
  (**pending deprecation**).
  An event listener is added for every exercise, thus when this message is received, all exercises will be reloaded.
  The message is accepted from any iframe (i.e. `origin='*'`).

  **N.B**: This will be deprecated, once there is a replacement in the Event API.

* `{type: 'a-plus-bind-exercise', id: exercise_element.id}`
  (**DEPRECATED**, use Event API).
  This is send just after `aplus:exercise-ready` event.
  The element can be retrieved with `document.getElementById(event.data.id)`.
