## TABLE OF CONTENTS

* [Automated Testing and Validation](#automated-testing-and-validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JavaScript Validation](#javascript-validation)
    * [Python Validation](#python-validation)
    * [Lighthouse Report](#lighthouse-report)
        * [Desktop](#desktop)
        * [Mobile](#mobile)
    * [WAVE Web Accessibility Evaluation Tool](#wave-web-accessibility-evaluation-tool)
    * [Django Automated Testing](#django-automated-testing)
        * [Coverage](#coverage)
* [Manual Testing](#manual-testing)
    * [Testing User Stories](#testing-user-stories)
    * [Full Testing](#full-testing)
* [Bugs, Errors & Solutions](#bugs-found-during-testing-and-development-phase)
    * [Solved Bugs](#solved-bugs)
    * [Known Bugs](#known-bugs)
---

## <strong>Testing</strong>
- [W3C Markup Validation Serice](https://validator.w3.org/) was used to test for error codes in the HTML.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)  was used to test for error codes in the CSS.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to detect errors and potential problems in Python code.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    was used during the development process to test, debug, explore and modify HTML elements, and to test responsiveness in different screen sizes.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used for improving the quality of web page. It has audits for performance, accessibility, progressive web apps, SEO, and more.


## Automated Testing and Validation
### HTML Validation
We used [W3C Markup Validation Service](https://validator.w3.org/) to validate all the HTML files by direct input:
|Page |Pass/Fail | images |
| ------------- | ------------- |------------- |
| Index | :heavy_check_mark: | |
| Register |:heavy_check_mark: | |
| Login |:heavy_check_mark: ||
| Logout |:heavy_check_mark: ||
| Profile |:heavy_check_mark: ||
| All Products|:heavy_check_mark: ||
|Product Detail |:heavy_check_mark: ||
|Add Product (admin) |:heavy_check_mark: ||
| Edit Product (admin) |:heavy_check_mark: ||
| Shopping Bag |:heavy_check_mark: ||
| Checkout |:heavy_check_mark: ||
| Order Success |:heavy_check_mark: ||
|Contact Us|:heavy_check_mark: ||
|Poll|:heavy_check_mark: ||
|Poll Success|:heavy_check_mark: ||
|Poll Result|:heavy_check_mark: ||
|Poll Create |:heavy_check_mark: ||


### CSS Validation
We used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate all CSS files by direct input.

|Page | Mobile  | Computer|
| ------------- | ------------- |------------- |
| Index | :heavy_check_mark: |<img src="markdown/htmlvalidation.png"> |
| Register |:heavy_check_mark: | <img src="markdown/htmlvalidation.png">|
| Login |:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|
| Logout |:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|
| Profile |:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|
| All Products|:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|
|Product Detail |:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|
|Add Product (admin) |:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|
| Edit Product (admin) |:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|
| Shopping Bag |:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|
| Checkout |:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|
| Order Success |:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|
|Contact Us|:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|
|Poll|:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|
|Poll Success|:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|
|Poll Result|:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|
|Poll Create |:heavy_check_mark: |<img src="markdown/htmlvalidation.png">|

### JavaScript Validation
We used [JSHint](https://jshint.com/) to validate all JavaScript and JQuery files
| Page | Result | Test Details & Screenshots |
| ---- | :-: | -------------------------- |
| [add-here-js-file-path] | [add-here-if-error-number] error and [add-here-if-warning-number] warning | [add-here-validation-image] |

### Python Validation
At the project inception, we installed [PyCodeStyle](https://pycodestyle.pycqa.org/en/latest/intro.html#configuration) in our workspace fixed errors when encountered throughout the development process. We also used [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) to lint our Python code.

| Application | Pass | Images |
| ------------- | ------------- |------------- |
| Bag |:heavy_check_mark: | <img src="markdown/pythonvalidation.png" height="60"> |
| Checkout |:heavy_check_mark: | <img src="markdown/pythonvalidation.png" height="60"> |
| Contact |:heavy_check_mark: | <img src="markdown/pythonvalidation.png" height="60"> |
| DaysComing |:heavy_check_mark: |  <img src="markdown/pythonvalidation.png" height="60">|
| Home | :heavy_check_mark: | <img src="markdown/pythonvalidation.png" height="60"> |
| Polls | :heavy_check_mark: | <img src="markdown/pythonvalidation.png" height="60"> |
| Products| :heavy_check_mark: | <img src="markdown/pythonvalidation.png" height="60"> |
| Profiles | :heavy_check_mark: | <img src="markdown/pythonvalidation.png" height="60">|


### Lighthouse Report
[Chrome DevTools' Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to test the performance, accessibility, best practices and SEO of the site

### <u>Lighthouse</u>
|Page | Mobile  | Computer|
| ------------- | ------------- |------------- |
| Index | | |
| Register | | |
| Login | ||
| Logout | ||
| Profile | ||
| All Products| ||
|Product Detail | ||
|Add Product (admin) | ||
| Edit Product (admin) | ||
| Shopping Bag | ||
| Checkout | ||
| Order Success | ||
|Contact Us| ||
|Poll| ||
|Poll Success| ||
|Poll Result| ||
|Poll Create |||


In order to fully validate the page, we used the WAVE Chrome extension. This enabled our team to test the pages that require user authentication.

| Page | WAVE This Page Result |
|Page | Computer|
| ------------- | ------------- |
| Index | | 
| Register  | |
| Login |  |
| Logout  | |
| Profile | |
| All Products | | 
| Product Detail | |
| Checkout | | 
| Shopping Bag  | |
| Order Confirmation | |
| Contact Us | | 
| Poll | | 
| Poll Success | | 
| Poll Results | | 
| Poll Create | | 
