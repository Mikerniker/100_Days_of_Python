#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


final_letters = []
final_numbers = []
final_symbols = []

for letter in range(1, nr_letters + 1):
  total_letters = len(letters) 
  random_letter = random.randint(0, total_letters - 1)
  final_letters += letters[random_letter]

for number in range(1, nr_numbers + 1):
  total_numbers = len(numbers)
  random_number = random.randint(1, total_numbers - 1)
  final_numbers += numbers[random_number]

for number in range(1, nr_symbols + 1):
  total_symbols = len(symbols)
  random_symbol = random.randint(1, total_symbols -1)
  final_symbols += symbols[random_symbol]

password = final_letters + final_numbers + final_symbols
random.shuffle(password)
final_password = "".join(password)
print(f"Here is your password: {final_password}")
