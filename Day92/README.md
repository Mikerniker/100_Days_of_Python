# IN PROGRESS
# Day 92 Professional Portfolio Project: Image Colour Palette Generator


## Overview

- Topics: Python, Flask

### The challenge

- Build a website where a user can upload an image and tell them what the top 10 most common colours in that image are.
 
### Links

- Solution URL: [Image Colour Palette Generator](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day92)

## Reflection
**Approach, Challenges, Learnings, and Future Improvements:** 
I approached the task by first creating the UI frontend using w3.css. The main challenge was figuring out how to extract colors from an image and convert them into hexadecimal values. This was a bit tough for me so I used a [reference](https://curbal.com/curbal-learning-portal/extract-colors-from-a-web-image-using-python) that employed pandas and PIL, and then I adapted the solution by converting it into functions that dynamically accept user input. This also allowed me to review and learn how to use the PIL library for image processing and integrating it with pandas.  Future improvements could focus on optimizing the color extraction process and enhancing the user interface.


## References
- [File Type](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file#unique_file_type_specifiers)
- [Add background color to TD](https://www.w3schools.com/tags/tag_td.asp)
Extract colors from image https://curbal.com/curbal-learning-portal/extract-colors-from-a-web-image-using-python