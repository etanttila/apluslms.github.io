# A+ material protocol version 1

## Terminology

* A _material_ is an interactive electronic book or workbook used by a course.
  A _material_ contains multiple _chapters_.

* A _chapter_ is a single page of the _material_, e.g., a single HTML document.
  A _chapter_ may include any number of interactive elements and _exercises_.

* A _client_ is the browser or the LMS application, which retrieves _chapters_.
  However, for the LMS the processing can be split between the browser and the server, e.g, the LMS retrieves the document, but the browser embeds exercises.

## Requesting a chapter

Chapters are retrieved one by one from the server storing the documents (aka., the content server).
The browser or the LMS makes an HTTP GET request to the configured URL.

The request must have the following headers:

* `X-Aplus-Event` (mandatory) must be `aplus.material.v1/retrieve-chapter`
* `User-Agent` (recommended) should contain the name and the version of the client and any other relevant details, e.g., `a-plus/1.7 (+https://aplus.example.com/) python-requests/2.24.0`.
  Note that you can not change the value for requests from the browser.
* [If-Modified-Since](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Modified-Since)

Additionally, the following query parameters may be part of the request:

* `lang` (recommended)
  is an [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag).
  The value for `lang` must match the value, which was used to configure the chapter URL in the LMS.
  Typically, the value is an [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) code, e.g., `en` or `fi`.


## The response document

The response should be an HTML document representing the chapter including:
markers for exercises and interactive elements, links to required CSS files, and script elements with valid source addresses.

If there exists an element with `class="chapter"` or `id="chapter"`, then contents of that element are shown to the user.
Otherwise, the contents of the `body` are shown.

The response may have the following headers:

* [Expires](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expires)
* [Last-Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Last-Modified)


### Exercise types

The following special attributes can be used to mark exercises.

* `<div data-aplus-exercise="[exercise-reference]"></div>`
  is used to mark a position of an exercise.
  The `[exercise-reference]` is a string, which should match the exercise name in the same path.
  For example, `data-aplus-exercise="ex1"` in a chapter with path `/foo/bar/` would find an exercise from path `/foo/bar/ex1`.

  The client should keep rest of attributes of the element in place.
  For example, the client could remove all child elements and add the interactive exercise component as a child, thus keeping the original element as is.

* `data-aplus-active-element`
  marks the exercise to be a type of Active Element.

* `data-aplus-quiz` (**pending deprecation**).
  When A+ sees an exercise div in an chapter with this attribute, it will use a different logic to load the exercise.
  This "questionnaire" method replaces the initial form with the last feedback.
  Instead, the LMS should provide UI where feedback is shown by default in place of the initial form, if the feedback contains a form.
  Though, there should be a "return" button to show the initial form again (aka., "reset" button).

* `data-aplus-ajax` (**pending deprecation**).
  Stops A+ from binding to the submit event of the exercise form and adding group selection and so on.
  May be used when the course JavaScript takes care of that.


### Special data attributes

The LMS should handle the following special data attributes.

* `data-aplus`.
  Any elements in the `head` containing this attribute, will be copied over to the document head, i.e, rest of the head elements are ignored.

* `data-aplus-chapter`
  is a hack to fix relative urls (**pending deprecation**).
  Assuming we have two files `/first.html` and `/second.html`, which are assumed to be served as `/first/` and `/second/`.
  Then, links in `/first/` are pointing to `/second.html`, which is not valid, thus they are replaced with links to `/second/`.
  This fix is only applied to links and images, when the have the attribute.

* `data-aplus-path`
  is a hack to fix relative urls (**pending deprecation**).
  The value is something like `https://server/{course}/`,
  where `{course}` is replaced with the first element of the path of the exercise url,
  e.g., for exercise url `http://grader/a001/ex01/foo` the `course` is `a001`.
  The value is finally joined to the exercise url with `urljoin`.
  The function is approximately this:

  ```python
prefix = element['data-aplus-path'].replace('{course}', exercse_url_first_path)
path = prefix + element['href'] # or 'src' for images
element['href'] = urljoin(exercise_url, path)
```

* `data-aplus-no-summary`.
  The A+ will hide the header above the exercise, when this attribute is specified.
  However, A+ will still add the default bindings.
  When added to, then the exercise frame title is hidden by the CSS.

Following attributes are reserved for the client, thus do not use them in the document:

* `data-aplus-overlay`
* `data-aplus-submit-disabled`
* `data-aplus-group`
* `data-aplus-group-fixed`


### An example of the document

```html
<!DOCTYPE html>
<html lang="en" >

<head>
  <meta charset="utf-8" />
  <title>My first chapter</title>

  <!-- head elements with `data-aplus` will be copied to the browser view -->
  <link data-aplus
    rel="stylesheet"
    type="text/css"
    href="https://content.example.com/mycourse/styles.css">
  <script data-aplus
    type="text/javascript"
    src="https://content.example.com/mycourse/interactive.js"
    async></script>

</head>

<body>
  <!--
    contents of the body will be used as there are no elements with
    id="chapter" or class="chapter"
  -->
  <h1>My first chapter</h1>
  <p>
    We talked about setup in
    <a data-aplus-chapter href="previous.html">the previous chapter</a>
  </p>

  <h2>The exercises</h2>

  <p>First, here is a normal exercise</p>
  <div data-aplus-exercise="ref-for-normal-exercise">
    The client is responsible for replacing this element with the actual exercise.
    If this content is visible, then the JavaScript or the LMS has a faulty code-
  </div>

  <p>Second, here is an questionnaire</p>
  <div data-aplus-exercise="ref-for-quiz" data-aplus-quiz>
    The client is responsible for replacing this element with the actual exercise.
    If this content is visible, then the JavaScript or the LMS has a faulty code.
  </div>

</body>

</html>
```
