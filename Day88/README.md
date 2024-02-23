# Day 88 Professional Portfolio Project: Cafe and Wifi Website


## Overview

- Topics: Python, Flask, SQLAlchemy, REST APIs, Web Development  

### The challenge

- Build a website that lists cafes with wifi and power for remote working.
- Use an SQLite database called cafes.db that lists cafe data and build a fully-fledged website to display the information in the database. It should display the cafes (optional: it could also allow people to add new cafes or delete cafes).

### Links

- Solution URL: [Cafe and Wifi Website](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day88)

## Reflection
**Approach & Challenges:** 
Designing the website was fun. The biggest challenge was resolving some initial errors, particularly getting Flash in Flask to work and formatting the tables to correctly display the information.

**Biggest learning:**

The biggest learnings include becoming more familiar with WTF Flask and reviewing Bootstrap 5 and its classes. Also, reviewing how to access and render the database information.

**Future Improvements:**
- Fix error handling.
- Add a check to verify if a cafe inputted by the user already exists in the database.
- Figure out how to adjust the width of the input box with render_form for a better UI. (I got a bit stuck here and couldn't seem to figure out how to fix this).

## Notes:
- Chanded accordion button by adding css; Did this to align it to the center and remove the arrow):
```
.accordion-button {
    display: initial;
    /* Other styles if needed */
}
``` 
- The ```me-2``` class adds margin to the right side of the input field/ creates space between the input field and the button.
- Adding a placeholder in Flaskform:
```
class SearchForm(FlaskForm):
    search_item = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Search for a cafe"})
```
- Also changed ```''``` to ```label=''``` since it caused an error rendering flash

## References:
- [Bootstrap-Flask Reference](https://python-adv-web-apps.readthedocs.io/en/latest/flask_forms.html)
- [Placeholder WTF](https://stackoverflow.com/questions/9749742/wtforms-can-i-add-a-placeholder-attribute-when-i-init-a-field)
- [Render WTF without Label](https://stackoverflow.com/questions/49037015/is-posible-to-render-wtf-form-field-with-out-label)
- [Change color of Flask messages](https://stackoverflow.com/questions/44569040/change-color-of-flask-flash-messages)
- [Formatting Bootstrap WTF Forms](https://bootstrap-flask.readthedocs.io/en/stable/macros/)
[Bootstrap Utilities Sizing](https://getbootstrap.com/docs/5.0/utilities/sizing/)  - used this to adjust length of the search (input) bar in initial design (but was later modified to render_form)
examples ```w-50 , w-75 , w-100 , or w-auto``` . This is all called Bootstrap Utilities Sizing
to adjust length of the search (input) bar
