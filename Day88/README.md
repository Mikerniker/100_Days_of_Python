# IN PROGRESS

# Day 88 Professional Portfolio Project: Cafe and Wifi Website


## Overview

- Topics: Python 

### The challenge


### Links

- Solution URL: [Cafe and Wifi Website](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day88)

## Notes
**Approach** 

**Challenges:** 

**Biggest learning:**


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