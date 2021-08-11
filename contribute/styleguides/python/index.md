# Python

First, read the [PEP 20: The Zen of Python](https://www.python.org/dev/peps/pep-0020/).

Python has an official and very comprehensive documentation about the style in [PEP 8](https://www.python.org/dev/peps/pep-0008/).
Rulings and styles stated in PEP 8 should be used by default, but with the following adjustments and emphases.

Let's start with some key quotes from the start of the PEP 8.

> One of Guido's key insights is that code is read much more often than it is written.

> However, know when to be inconsistent -- sometimes style guide recommendations just aren't applicable.
> When in doubt, use your best judgment.
> Look at other examples and decide what looks best.
> And don't hesitate to ask!

For that, remember these good reasons to ignore a particular guideline:

1. Applying the guideline would make the code less readable, even for someone who is used to reading code that follows this style guide.
1. Being consistent with surrounding code that also breaks it (maybe for historic reasons).
   * However, this is also an opportunity to clean up someone else's mess.
     Hence, consider if the change is small enough that refactoring wouldn't be wise.
1. The code in question predates the introduction of the guideline and there is no other reason to be modifying that code.
   I.e. don't fix styles in existing files beforehand.

## Indentation, line length, and blank lines

Use **4 spaces** per indentation level.
Try to limit lines to **79** characters, and don't exceed **119** characters.
Furthermore, for long blocks of text (such as docstrings and comments), aim to keep the line length under **72** characters to make the text more readable for humans by limiting the column width.

Split too long lines to multiple lines and indent appropriately, but don't do it needlessly.
In addition, use a longer line (not exceeding 119 characters), if the code is more readable that way!
You can also use temporary variables to split longer lines to parts, which adds documentation too (in the form of variable names).

**Try to keep `if` statements in a single line**, because there are no good ways to split them to multiple lines.
However, if you must split an `if`, then use a syntax that makes the code most readable.
Consult the PEP 8 and this document for ideas.

**Do not use a backslash** for line continuation, unless it's the only option.
The preferred way of wrapping long lines is by implied line continuation inside parentheses, brackets and braces.
Long lines can be broken over multiple lines by wrapping expressions in parentheses.

```python
# BAD:
foo = "a long string and some more" if not is_active \
      else "another long line, which makes this a pretty long line"
# better:
foo = ("a long string and some more"
       if not is_active
       else "another long line, which makes this a pretty long line")
# or:
if not is_active:
    foo = "a long string and some more"
else:
    foo = "another long line, which makes this a pretty long line"
```

However, **with statements** are a good example where backslashes are good.
Sadly, these also break the "one line per item" rule, but this is still the preferred way.
Furthermore, if you use this layout, then keep every assignment on it's own line.

```python
with open('in.txt', 'r') as in_file, \
     open('out.txt', 'w') as out_file, \
     get_some_cool_thing() as filter:
    out_file.write(filter(in_file.read()))
```

NB:
Remember [contextlib.ExitStack](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack) as it might be a better alternative for a bit more complex case.

```python
from contextlib impport .ExitStack

with ExitStack() as stack:
    # open all files before reading any of them
    in_files = [stack.enter_context(open(fn, 'r')) for fn in files_to_read]
    out_file = stack.enter_context(open('out.txt', 'w'))
    # all files can be read and output written, so do the actualy thing
    for in_ in in_files:
        out_file.write(in_.read())
```

**Use space to help with perception**, i.e., blank lines should be used to group related parts and to distance separate ones.
Separate top-level function and class definitions with **two** blank lines.
Method definitions inside a class are separated by **a single** blank line.
In addition, use a single blank line to add space between logical blocks of the code.
See [Wikipedia/Principles of Grouping](https://en.wikipedia.org/wiki/Principles_of_grouping)) to understand why this is important.

To expand those rules a bit, here are three deviations:
1. Extra blank lines may be used (sparingly) to separate groups of related functions.
1. Comments may be used to separate bigger parts of the code.
1. Blank lines may be omitted between a bunch of related one-liners (e.g. dummy implementations) and variable definitions, even in the top level.

**Use comments to explain why**, not what.
It's often enough to write a short reason in the comment, as long as the longer description is in the git commit message, where it should be.
In contrast, the code should explain what is done, thus remember to use clear variable and function names.
Additionally, avoid inline comments.
It's often better to dedicate a line for the comment.

Example demonstrating whitespace and comments:

```python
import logging
from sys import environ

import django
from django.conf import settings


logger = logging.getLogger(__name__)


# In place like this, you could use a comment, without extra space below.
foo = lambda x: x*x
bar = lambda x: s.strip()
baz = kambda x: x+2


def helper(x):
    return x


## Classes for the public API
# you may use space and extra # to make a comment stand out
# for example, that now looks like a title

class MainClass:
    """A class documentation
    """
    def __init__(self):
        pass

    def method(self, a):
        # NOTE: hack() fixes a rendering issue
        return foo(a) if hack() else baz(a)


if __name__ == '__main__':
    MainClass().method(3)
```

## One line per item

Try to ensure that changes in the future will not require changes to adjacent lines, thus git commits – now and in the future – should only include the lines related to the logical change.
When listing elements on several lines, if it's possible to add new elements to the end of the list in the future, there should be a comma after the last entry (to allow adding new elements to the list without having to add a comma to the previous line).
This  also means that you should try to avoid listing entries in a single line, though it is ok for a very short list.

Example demonstrating listing as well as indentation in different contexts of lists
```python
# short list/args are fine
foo = [1, 2, 3]
bar(1, 2, 3)

# longer lists, should have a single entry per line
foo = [
    "first thing",
    "a second thing",
    "some things more", # don't forget the comma!
] # put the closing bracket back here

# the same can be done for functions and can be nested
result = bar(
    "first positional",
    None,
    keyword1='value', # note: no space around =
    foobar={
        'key': "a value",
    },
)

# when defining functions (note the extra indent)
def foobar(
        argument1,
        argument2,
        keyword1=None,
        keyword2=None, # remember the comma
        ): # here this seems to be part of the arguments, which is good
    if keyword1 is None:
        # not a style thing, but set defaults in the function
        keyword1 = {}
    return banana(argument1, argument2, banana=keyword1)

# chained method calls
foobar = (
    MyObject
    .method1(arg1, arg2)
    .method2(
        keyword1="a long line here for a reference",
        ketword2=42,
    )
)

# however, if the last element won't _ever_ change, i.e., there is no need to
# add anything after it.
foobar = (MyModel.objects
          .filter(id=3)
          .distinct()
          .all()) # "all" is _always_ the last

# same applies to imports
from foo import (
    bar,
    baz,
)
# two can be kept in a single line
from foo import bar, baz
# remember the import order!
```

However, ***argparse*** breaks the above rule and a compact format should be used instead.
This is for couple of reasons:
Firstly, the compact list is easier to read as the first line contains the most significant information.
Secondly, the arguments are normally permanent after release, thus there typically aren't any changes later on.
Lastly, many programs already use the format, thus people have trained to read it.

To ensure the readability, try keeping the arguments in the following order:
* First, the most defining bits in the first line: name/flags, metavar, dest, and action.
* Then add any other arguments.
* Lastly, set the `help` and split really long lines nicely.

```python
def SomeClass:
    def method(self, parser):
        # The following line is few characters too long, but it's often
        # better than the alternative
        parser.add_argument('-s', '--sum', dest='accumulate', action='store_const',
            const=sum, default=max,
            help="Define the used accumulator for numbers. "
                 "Set to 'max' to find the maximum number or "
                 "to 'sum' to find the sum of the numbers. "
                 "(default: max)")
        parser.add_argument('numbers', metavar='N', type=int, nargs='+',
            help='an integer for the accumulator')
```

### Operators come after line breaks

To help readability, write operators after a new line.
In addition, this helps with the one item per line rule.

Example demonstrating usage of operators (line changes, indentation and commenting):

```python
has_permissions = (
    user is not None
    and user.is_authenticated
    and (
        # is an administrator
        user.is_superuser
        # or is a teacher
        or (
            isinstance(user, User)
            and course.teachers.filter(id=user.userprofile.id).exists()
        )
        # or is an assessment tool
        or (
            isinstance(user, GraderUser)
            and user._course == course
        )
    )
)

total_cost = (
    sum(item.cost for item in items)
    + (value * tax)
    - coupon
)
```

## File structure

 1. Module doc string
 2. from future imports (document when feature is optional and mandatory)
 3. module dunder names (e.g. `__all__`)
 4. normal imports

    1. standard library imports
    2. 3rd party library imports
    3. project imports (only relevant with Django)
    4. relative imports

    [//]: # (TODO imports should be moved to it's own paragraph)

 5. public helpers
 6. public classes
 7. private helpers
 8. private classes
 9. module level initialisation (after a class, there can be edits to that specific class)
10. the `if __name__ == '__main__'`

```python
"""
This is a python module
"""

from __future__ import annotations # py3.7 .. py4.0

__version__ = '1.0'

import os.path
import sys
from collections import OrderedDict

import hanks_cool_lib
from django.conf import settings

from webshop.models import Shop
from .utils import helper


def parse_input(str):
    return Parser(str).parse()


class Parse:
    def __init__(self, input):
        self._input = input

    def parse(self):
        return _split(str)


def _split(str):
    return str.splitlines()


if __name__ == '__main__':
    import sys
    print(parse_input(sys.stdin.read()))
```

## Quotes

In general, you may use single and double quotes in a way that comes naturally to you. This is because they don't
really affect readability. However, these need to be followed, as they affect readability:
* use single quote for strings if they contain double quotes and vice-versa
* except, when string contains both quotes, then use quotes with
  escaping

In case that you do not have a particular preference to quote usage or want instructions anyway, use the following:
* double quote (`"`) for strings shown to the user
* single quote (`'`) for everything else

Example demonstrating proper use of quotes:

```python
d['key'] = 'type'
message1 = "this is a message"
message2 = 'you should use " -characters instead'
message3 = "mix of \" and ' quotes should be like this"
message4 = "file '{filename}' was not found"
message4 = "file {filename!r} was not found" # ok if filename is always a string
```

## String formatting

If the project may require python 3.6, then f-string ([PEP 498](https://www.python.org/dev/peps/pep-0498/)) can be used.
However, if the string uses translations, then formatting must be done after translation lookup, thus f-string is not an option.

Typically, the code should prefer f-string due to them being more concise and readable.
Remember, when using lazily evaluated strings, then the formatting should be lazy too.
For example, django `gettext` returns a lazy object, hence `format_lazy` should be used with it.

The printf-style formatting should be typically avoided, but can be used for data processing and exceptions.
Always remember to pass a single argument as a tuple (e.g. `"name is %s" % (name,)`).


```python
# preferred order:
# fastest and simplest (only if py3.6 is possible)
', '.join(f"{k}:{v}" for k, v in d.items())
# second best alternative (̃~15% slower than the f-string):
', '.join("%s:%s" % (k, v) for k, v in d.items())
# slow and unclean (~40% slower than the f-string):
', '.join("{}:{}".format(k, v) for k, v in d.items())
# really bad (~65% slower than the f-string):
', '.join(str(k)+":"+str(v) for k, v in d.items())
```

## Assignment expression

Assuming the project is able to require Python 3.8, then the assignment
expression ([PEP 572](https://www.python.org/dev/peps/pep-0572/)) is
acceptable. However, avoid using the feature just because you can. The PEP 572
includes many examples of good and bad usage. Do not use the expression, if
there is only minimal benefits.

```python
# avoid using for cases, that are too simple
total = value := sum(items) + value*tax

# would this be more readable?
value = sum(items)
total = value + value*tax
```

However, there are really good uses, e.g., multiple regex matches:

```python
if match := re.search('^foo', str):
    do_foo(match.group(0))
elif match := re.search('^bar', str):
    do_bar(match.group(0))
elif match := re.search('^baz', str):
    do_baz(match.group(0))
```

## Version requirements

Version requirements are defined in `requirements*.txt` files and in `setup.py`.
For these, there should be spaces around the operators (like in normal Python code) to make the requirements more readable.
Avoid using the `==` notation if possible as it prevents bugfixes from being installed.

```
package-one == 1.2.0      # strict requirement, typically too strict
package-two >= 2.1, < 2.2 # multiple requirements can be set
package-tre ~= 2.1.1      # same as >= 2.1.1, == 2.1.*
```

The [PEP 440](https://www.python.org/dev/peps/pep-0440/) explains more about the topic.

### Doc strings

[//]: # (TODO rethink if this a good layout)

```python
def function(arg1, arg2, arg3=None, *, arg4=None):
    """Function takes arguments and produces a result

    You may describe more stuff here.

    :param arg1: and you may add explanation about different arguments
    :type arg1: don't write types here, use python3 type annotations instead
    :return: returns a monster value (type annotation might be enough)

```

## Naming

```python
# Globals have only uppercase letters and underscores.
A_GLOBAL = True

# Functions and methods have only lowercase letters and underscores.
def a_function(a_argument):
    in_, _dot, _ext = a_argument.rpartition('.')
    # avoid keywords, but if needed, add underscore in the end of it (in_)
    # don' use just _ for unused variables, add also a name (_dot)

def _non_public_function():
    pass

def AClass:
    # for constant values use uppercase like with globals
    LIKE_A_GLOBAL = True
    # for configurable variables and such, use lowercase
    just_an_class_variable = True

    def a_method(self):
        pass

    def _non_public_method(self):
        # this method is not part of the public API
        # rarely, this can be used to namespace things
        # (see collections.namedtuple)

    def __namespaced_method(self):
        # The real method name will be __AClass_namespaced_method
```

Use English and ASCII for identifiers, even though Python allows unicode characters.

Example of what not to do:

```python
def öö(minä):
    print(minä)
öö("¿ʇɥƃᴉɹ 'ɹǝʌǝlɔ sɐʍ sᴉɥʇ")
```

## Django, Flask, and other framework specific details

* [HTML templates](../html/#django-and-jinja-templates)
* [gettext tanslations](../gettext/)
