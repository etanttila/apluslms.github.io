# A+ questionnaire feedback protocol version 1

This is a styling support for questionnaire like exercises.
These classes may be used in the feedback HTML, when the content is inside an element with `class="aplus-quiz1"`.
The following classes and nested classes are defined:


* `.error-summary`
* `.error-summary .error-summary__text`
* `.error-text`
* `.has-error .checkbox`
* `.has-error .radio`
* `.hint-checkbox`
* `.option-checked`
* `.question-area`
* `.question-description`
* `.question-feedback`
* `.question-hint`

Additionally, following icons are supported:

* `<i class="quiz1-icon-correct"></i>` for a correct answer
* `<i class="quiz1-icon-neutral"></i>` for a neutral answer (not correct or incorrect)
* `<i class="quiz1-icon-incorrect"></i>` for an incorrect answer

See [a-plus/quiz1.scss](https://github.com/apluslms/a-plus/blob/master/assets/sass/protocols/_quiz1.scss) for a reference implementation.
