# Style Guides

## EditorConfig

[EditorConfig](https://editorconfig.org/) is a standard to let editors know about the basic settings for the project.
These include indentation type (spaces vs. tabs) and indentation width for example.
For a full list of fully and partially supported properties, see the [project wiki](https://github.com/editorconfig/editorconfig/wiki/EditorConfig-Properties).
All A+ LMS repositories should include an `.editorconfig`.

If the project does not include an `.editorconfig`, then one should be download from [.editorconfig](../../../editorconfig.ini).
Remember to send updates to [upstream]({{ site.github.repository_url }}) too!


## Style Guides for major languages

* [CSS and SCSS](css/)
  * indent: **tab**
  * identifier names: variables `$brand-success` and `--brand-success`, classes use [BEM](http://getbem.com/)
* (GNU) [gettext](gettext/) translations
* [HTML](html/)
  * indent: **tab**
* JavaScript
  * indent: **2 spaces**
  * max line length:, soft limit **79**, hard limit 99
  * identifier names: **PascalCase** for classes; **camelCase** for variables, functions and methods
* Python, Django and other Python frameworks
  * indent: **4 spaces**
  * max line length: text blocks 72, soft limit **79**, hard limit 119
  * identifier names: **PascalCase** for classes; **snake_case** for variables, functions and methods
