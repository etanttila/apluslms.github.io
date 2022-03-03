---
nav-group: community
nav-weight: 4
---
# Style Guides

## EditorConfig

[EditorConfig](https://editorconfig.org/) is a standard to let editors know about the basic settings for the project.
These include indentation type (spaces vs. tabs) and indentation width for example.
For a full list of fully and partially supported properties, see the [project wiki](https://github.com/editorconfig/editorconfig/wiki/EditorConfig-Properties).
All A+ LMS repositories should include an `.editorconfig`.

If the project does not include an `.editorconfig`, then one should be download from [.editorconfig](../../../editorconfig.ini).
Remember to send updates to [upstream]({{ site.github.repository_url }}) too!


## Style Guides for major languages

[A+ Design System](https://apluslms.github.io/a-plus-design-system/)
showcases consistent, robust and accessible components and styles for building in the A+ ecosystem.

* [CSS and SCSS](css/)
  * indent: **tab**
  * identifier names: variables `$brand-success` and `--brand-success`, classes use [BEM](http://getbem.com/)
* (GNU) [gettext](gettext/) translations
  * [Frequently used translations](../frequently_used_translations.md)
* [HTML](html/)
  * indent: **tab**
* JavaScript
  * indent: **2 spaces**
  * max line length:, soft limit **79**, hard limit 99
  * identifier names: **PascalCase** for classes; **camelCase** for variables, functions and methods
* [Python](python/), Django and other Python frameworks
  * indent: **4 spaces**
  * max line length: text blocks 72, soft limit **79**, hard limit 119
  * identifier names: **PascalCase** for classes; **snake_case** for variables, functions and methods
