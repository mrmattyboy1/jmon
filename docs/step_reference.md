
# Step Reference

Each of the following elements can be included in the step templates.

Compatibility between clients differ and compatibility across all used elements must contain a common client.



## GotoStep

Key: `goto`


Directive for loading a page.

This should generally always be used as a first directive of a step.

It can be used multiple times during a check.

This can be placed in the root of the check, e.g.
```
 - goto: https://example.com
 - find:
   - tag: input
   - url: https://example.com/?followed=redirect

 - goto: https://example.com/login
```


Client Support: `BROWSER_FIREFOX`, `BROWSER_CHROME`, `REQUESTS`

## FindStep

Key: `find`


Directive for finding an element of a page.

Each find can use on of the following attributes, some of which can be combined:
 * `id` - Search by ID of element on the page.
 * `class` - Search for element by class name.
 * `text` - Search for element by visible text. Can be combined with `tag`.
 * `placeholder` - Search for input element by placeholder value. Can be combined with `tag`.
 * `tag` - Search for element by tag (e.g. `a` for links). Can be combined with `placeholder` or `text`.

If an element cannot be found using the given parameters, the step will fail. No `check` action is required for validating this.

This can be placed in the root of the check, e.g.
```
 - goto: https://example.com
 - find:
   - tag: input
   - url: https://example.com/?followed=redirect
```

Find elements can be nested to find elements within other elements. E.g.:
```
 - goto: https://example.com
 - find:
   - id: content
   - find:
     - class: loginForm
     - find:
       - tag: input
       - placeholder: Username
```


Client Support: `BROWSER_FIREFOX`, `BROWSER_CHROME`

### ActionStep

Key: `actions`


Directive for performing an action task.

Each action directive may one or more actions.

This can be placed in the root of the check, e.g.
```
 - goto: https://example.com
 - actions:
   - click
```

It can also be placed within a find directive, e.g.:
```
 - goto: https://example.com
 - find:
   - tag: input
   - actions:
     - type: Pabalonium
     - press: enter
```


Client Support: `BROWSER_FIREFOX`, `BROWSER_CHROME`

#### ClickAction

Key: `click`


Directive for clicking the current element, simulating a mouse left-click.

E.g.
```
- goto: https://example.com
- find:
  - id: login
  - actions:
    - click
```


Client Support: `BROWSER_FIREFOX`, `BROWSER_CHROME`

#### TypeAction

Key: `type`


Directive for typing characters into the selected element.

Supported keys:
 * `enter`

E.g.
```
- goto: https://example.com
- find:
  - id: login
  - actions:
    - click
    - type: my-username
```


Client Support: `BROWSER_FIREFOX`, `BROWSER_CHROME`

#### PressAction

Key: `press`


Directive for pressing buttons, simulating a keyboard button press.

Supported keys:
 * `enter`

E.g.
```
- goto: https://example.com
- find:
  - id: login
  - actions:
    - press: enter
```


Client Support: `BROWSER_FIREFOX`, `BROWSER_CHROME`

#### ScreenshotAction

Key: `screenshot`


Directive for capturing a screenshot of the current page.

A value must be provided, which will be the name given to the screenshot.

This action can be performed multiple times.

E.g.
```
- goto: https://example.com
- actions:
  - screenshot: example
- goto: https://example.com/login
- actions:
  - screenshot: example-login
```


Client Support: `BROWSER_FIREFOX`, `BROWSER_CHROME`

### CheckStep

Key: `check`


Directive for performing a check task.

Each check directive may one or more checks.

This can be placed in the root of the check, e.g.
```
 - goto: https://example.com
 - check:
     title: Example Page
     url: https://example.com/?followed=redirect
```

It can also be placed within a find directive, e.g.:
```
 - goto: https://example.com
 - find:
   - tag: input
   - check:
       text: Enter input
```


Client Support: `BROWSER_FIREFOX`, `BROWSER_CHROME`, `REQUESTS`

#### TitleCheck

Key: `title`


Directive for verifying HTML page title.

E.g.
```
- goto: https://example.com
- check:
    title: "Example - Homepage"
```


Client Support: `BROWSER_FIREFOX`, `BROWSER_CHROME`

#### UrlCheck

Key: `url`


Directive for verifying current page URL.

E.g.
```
- goto: https://example.com
- check:
    url: https://example.com/redirect-was-followed
```


Client Support: `REQUESTS`, `BROWSER_FIREFOX`, `BROWSER_CHROME`

#### ResponseCheck

Key: `response`


Directive for verifying HTTP response code

E.g.
```
- goto: https://example.com
- check:
    response: 200
```


Client Support: `REQUESTS`

#### JsonCheck

Key: `json`


Directive for verifying the content of a JSON repsonse.

One of two validation attributes must be used:
* equals - Checks the value matches the provided content
* contains - Checks that the provided value is within the content.

A "selector" attribute may be provided to verify the value of a single element of the JSON response.
The selector uses the syntax provided by [jsonpath](https://pypi.org/project/jsonpath-python).
If a selector is not provided, the entire JSON response will be checked.

```
- check:
    json:
      selector: '$.images[0]'
      contains: 1.jpg

- check:
    json:
      selector: '$.id'
      equals: 1
```


Client Support: `REQUESTS`

#### TextCheck

Key: `text`


Directive for verifying text content.

E.g.
```
- goto: https://example.com
- check:
    text: "It's good"
```

This directive can be used within a find element. E.g.:
```
- goto: https://example.com
- find:
  - id: login
  - check:
      text: Please Login
```


Client Support: `BROWSER_FIREFOX`, `BROWSER_CHROME`