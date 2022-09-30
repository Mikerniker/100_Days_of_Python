## Debug the Leap Year Code:
- Fix the bug in the following code:

### ORIGINAL CODE with BUGS:

```
year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

```

#### My findings: The error was due to a type error for input.
#### The input needed to be converted to an integer, since it was initially saved as a string. Fixed code is in main.py
