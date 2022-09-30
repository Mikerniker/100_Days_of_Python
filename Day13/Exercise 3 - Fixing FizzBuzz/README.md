## Debugging FizzBuzz:
- Fix the bug in the following code:

### ORIGINAL CODE with BUGS:

```
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
```

#### My findings:
- 1st bug: The else statement printed the number in brackets, the brackets were removed to print the number.
- 2nd bug: The original code used "or" instead of "and" which affected what would be printed
- 3rd bug: Multiple if statements were used, this was changed to "elif" for some parts. 
- Fixed code is in main.py
