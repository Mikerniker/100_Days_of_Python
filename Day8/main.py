from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:    
    if not char.isalpha():
      end_text += char
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
  print(f"Here's the {cipher_direction}d result: {end_text}")

end_of_codes = False  
while not end_of_codes:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  cont_caesar = input("Do you want to go again? Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
  if cont_caesar != "yes":
    end_of_codes = True
  
  if shift > len(alphabet):
    shift %2 != 0
     

