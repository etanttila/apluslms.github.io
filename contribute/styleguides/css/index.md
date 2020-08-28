# CSS and SCSS (DRAFT)

**N.B.** this document is a bit draft, please contribute to make it more complete.

* Indent with **tabs**
* Use [BEM](http://getbem.com/) for class names
* Identifiers use hyphens, e.g., `$brand-success` and `--brand-success`
* Do not add styles for classes starting with `js-`, as they are _only_ for JavaScript.
  If you find adding styles for them, create a new class.

# SCSS and SASS

Generic notes:

* Use comments, as they are removed, except `/*! .. */`, which may be used to force newlines in `.min.css`.
* Use variables.
  If a value is not generic (e.g. not black, white, 0, or 1), then use a variable for it.
  You can first define the variable in the current element or the file, where it cam be moved to specific file when it's used more globally.

Order of things:

* (variables)
* extend
* include
* properties
* pseudo classes
* nested selectors

Keep all styles in component files, not in a table-of-contents file.

The order of includes in the table-of-contents (the root) file:

* variables (e.g., themes and colors)
* vendor
* authored dependencies
* patterns (aka., components)
* site parts (e.g., styles for single views)

In short, from more generic to specific rules.
