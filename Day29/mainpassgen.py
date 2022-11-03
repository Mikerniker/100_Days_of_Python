#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

#password_list = []

# new_letters = [random.choice(letters) for char in range(nr_letters)]
# new_symbols = [random.choice(symbols) for char in range(nr_symbols)]
# new_nums = [random.choice(numbers) for char in range(nr_numbers)]
# password_list = new_letters + new_symbols + new_nums


password_list = [random.choice(letters) for char in range(nr_letters)] + \
                [random.choice(symbols) for char in range(nr_symbols)] + \
                [random.choice(numbers) for char in range(nr_numbers)]


random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
