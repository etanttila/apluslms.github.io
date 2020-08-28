# HTML

An HTML does not have many important rules, but following these rules will make the life a bit easier.

## Basic rules for HTML

* Indent using tabs, as it takes less space on transit (HTML files are typically not minified).
* No line length limit, but be reasonable.
* You may split element attributes to multiple lines, though use good judgement on when to do that and how to split the attributes.
* If the element and it's text content can fit nicely in a single line, then do that.
  Otherwise, split it to multiple lines with opening and closing tags in their own lines (with the content indented).


### Example

```html
<form
    id="a-long-id-string"
    data-form-nonce="9c6b6e43-201e-4f57-bc77-48368a3a1fda"
    method="post"
    action="some/other/url/"
    enctype="multipart/form-data"
>
    <p>Submit some things</p>
    <div class="form-group">
        <label
            class="control-label"
            for="some-input-id"
            data-some-data="9c6b6e43-201e-4f57-bc77-48368a3a1fda"
        >
            Label
        </label>
        <input
            type="text"
            id="some-input-id"
            name="some-input"
            class="form-control"
            placeholder="Write some numbers here"
            inputmode="numeric"
            title="Only integers"
            pattern="[+-]?[0-9]+"
            value="0"
            required
        >
    </div>
    <div class="form-group">
        <input type="submit" value="Submit" class="btn btn-primary">
    </div>
</form>
```

## Django and Jinja Templates

* template blocks indent too

{% highlight jinja %}{% raw %}
<body>
    {% if something %}
        <h1>Conditional</h1>
        {% for x in y %}
            <p>The value of x is {{ x }}</p>
        {% endfor%}
    {% endif %}
</body>
{% endraw %}{% endhighlight %}

* add space in around variable names

{% highlight jinja %}{% raw %}
<p>{{ variable }}</p>
<p>{{ value|title }}</p>
{% endraw %}{% endhighlight %}

* use `trimmed` with blocktrans

{% highlight jinja %}{% raw %}
{% block content %}
    <div>
        <h1>{{ title }}</h1>
        {% blocktrans trimmed with foo=variable|filter %}
            Some text with uses {{ foo }} as part of it.
            Can have multiple lines.
        {% endblocktrans %}
        <p id="foo"
            class="class1 class2"
            data-foo="bar"
            data-baz="foo"
        >
            <span>Some text</span>
        </p>
        {% include %}
    </div>
{% endblock %}
{% endraw %}{% endhighlight %}

