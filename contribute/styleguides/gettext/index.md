# GNU Gettext Translations

The goal with following rules is to lower amount of problems when working with git.
Idea is not to update fields that do not add any value and fields that are not relevant for the change in a commit.

* Only `.po` files to git, i.e., no `.mo` files.

  * The `.mo` files should be compiled by the packaging system and locally during development.

* If no reason not to, use English string as message id (i.e. default string) and make translations for other languages (e.g. Finnish).  
  **NOTE:** Separate message keys are used in the Django translations of the `a-plus` repository, and translations are written for English as well.
  See section [msdID format](#msgid-format) for more details.
* Use translation tool, they format the file correctly.
  Or run a script which merges the `.po` files, which reformatting.
* Do not add line numbers, but add filenames, as it makes simple changes in the git.
  This can be done with the `--add-location=file` option in most gettext tools.
* No need to set or update meta headers at the top of a `.po` file, as those details are typically available from the git.
  However, if the translation was done by a non-git user, then those fields could be used.
  It's recommended to write those details in the commit message too (e.g., add the `Co-Authored-By` header).
* No need to keep obsolete translation strings, as they are in the git history.


## Django specific stuff

* Use `trimmed` in `blocktrans`
* Typical `makemessages` call:

  ```sh
  ./manage.py makemessages --ignore='venv*/*' --no-obsolete --add-location file
  ```


### msgID format

**NOTE:** This is currently in use only in the a-plus repository.

In order to make editing strings displayed to users easier (and less likely to break things), rather than using the English string as the message id, a separate key is used as a message id.

* The string key should be in all caps, different words separated by underscores (aka SCREAMING_SNAKE_CASE)
* If there are variables in the string (for string formatting), those are listed at the end of the string after two dashes (`--`), each variable separated with a comma.

  * In Django templates (HTML-files), the variables are surrounded by two curly brackets and spaces (`{{ var_name }}`).
    In the `.po` file, these strings will be marked as being in `python-format`, the surrounding spaces will be removed, and two curly brackets will be replaced to become `%(var_name)s`.
  * In Python files, the variables are surrounded by one curly bracket (`{var_name}`).
    In the `.po` file, these strings will be marked as being in `python-brace-format`.

  ```html
  {% blocktranslate trimmed with start=instance.enrollment_start end=instance.enrollment_end %}
    ENROLLMENT_OPEN_BETWEEN -- {{ start }}, {{ end }}
  {% endblocktranslate %}
  ```

  ```python
  messages.warning(self.request,
      format_lazy(
          _('DEVIATION_WARNING_DEADLINE_DEVIATION_ALREADY_FOR -- {user}, {exercise}'),
          user=str(profile),
          exercise=str(exercise),
      )
  )
  ```

  ```po
  #: course/templates/course/enroll.html
  #, python-format
  msgid "ENROLLMENT_OPEN_BETWEEN -- %(start)s, %(end)s"
  msgstr "Enrollment is open from %(start)s to %(end)s."
  
  #: deviations/views.py
  #, python-brace-format
  msgid "DEVIATION_WARNING_DEADLINE_DEVIATION_ALREADY_FOR -- {user}, {exercise}"
  msgstr ""
  "Deadline deviation already exists for {user} in {exercise}! Remove it before "
  "trying to add a new one."
  ```

* If the same word or phrase is used multiple times in the repository with different formattings (such as in lower case, capitalized, all caps, etc.), make sure to distinguish between these forms by adding the formatting instruction in **lower case** after the key

  ```po
  #: course/models.py templates/base.html
  msgid "HIDDEN_capitalized"
  msgstr "Hidden"

  #: edit_course/templates/edit_course/clone_instance.html
  msgid "HIDDEN_lowercase"
  msgstr "hidden"
  ```

* The first few words of the key are good for giving some context or meta information, which can be helpful when trying to understand where the message is used or for finding related or similar messages.
  (E.g. one can indicate if the messages relate to access and permissions, courses, modules, exercises, etc.)
  * If the string is a error message, a warning, or a message indicating success or failure, it's good to indidate that in the key.

  ```po
  msgid "ACCESS_ERROR_ONLY_TEACHERS"
  msgstr "Only teachers shall pass"

  msgid "DEVIATION_WARNING_MUST_PROVIDE_MINUTES_OR_FUTURE_DATE"
  msgstr "You have to provide either minutes or a date in the future."

  msgid "BUILD_LOG_ERROR_REQUESTING_FAILED -- {error!s}'"
  msgstr "Requesting build log failed with error '{error!s}'."

  msgid "SUCCESS_SAVING_MODEL -- {name}"
  msgstr "The {name} was saved successfully."

  msgid "FAILURE_SAVING_MODEL -- {name}"
  msgstr "Failed to save {name}."
  ```

* Often single words or short phrases will basically have the word or phrase itself as a key  
  e.g. `USER_RESULTS` ~ `User results`; `TABLE_OF_CONTENTS` ~ `Table of contents`
  * If there are enums or other groupings, it can be good to provide context with the first word.
    The 'individual' part can be the same or related to the variable name of the enum.  
    e.g. `NUMBERING_NONE` ~ `No numbering`, `NUMBERING_ARABIC` ~ `Arabic`, `NUMBERING_ROMAN` ~ `Roman`