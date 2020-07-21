# A+ hooks protocol version 1

The LMS sends web requests when specific events occur.
For example, after every submission, the LMS may notify services, which are configured in the LMS for the hook.

# Post Assessment Event

This event triggers after a submission receives an assessment, i.e., the state of the submission changes from pending state to assessed.
However, the event does not trigger when the state changes to any failure state.

The request must have the following headers:

* `Content-Type` (mandatory) must be `application/x-www-form-urlencoded`
* `X-Aplus-Event` (mandatory) must be `aplus.hook.v1/post-assessment`
* `User-Agent` (recommended) should contain the name and the version of the LMS and any other relevant details, e.g., `a-plus/1.7 (+https://aplus.example.com/) python-requests/2.24.0`

The body of the request must contain the following fields:

* `submission_id` is an identifier, e.g., `1001234`
* `exercise_id` is an identifier, e.g., `week1/ex01`
* `course_id` is an identifier, e.g., `mycourse/2020`
* `site` is an URL, e.g., `http://aplus.invalid`

Identifiers are strings, which identify the item in the context of the LMS installation at the `site`.
Identifiers may be used to filter hook requests  or retrieve more data from the LMS API.
