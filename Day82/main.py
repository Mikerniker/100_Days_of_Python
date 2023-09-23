morse_code = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",  "g": "--.", "h": "....",
              "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
              "q": "--.-", "r": ".-.", "s": "...", "t": "-",  "u": "..-", "v": "...-", "w": ".--",
              "x": "-..-", "y": "-.--", "z": "--..",
              "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
              "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----"}

def convert_to_morse():
    user_message = input("Enter your message: ").lower()
    message = list(user_message)

    coded_message = ""
    for letter in message:
        if letter.isalpha() or letter.isdigit():
            coded_message += morse_code[letter] + " "
        else:
            letter = "/ "
            coded_message += letter
    return coded_message


def decode_morse(code):
    coded_message = code.split()

    decoded_msg = ""
    for letter in coded_message:
        for key, value in morse_code.items():
            if letter == value:
                decoded_msg += key
        if letter == "/":
            decoded_msg += letter

    decoded = decoded_msg.split('/')
    return ' '.join(decoded).capitalize()


program_on = True

while program_on:
    print("Hello! Welcome to the Morse Code Decoder")
    convert_or_decode = input("Do you want to convert or decode Morse code, type: 'convert or decode': ").lower()
    if convert_or_decode == 'convert':
        morse_message = convert_to_morse()
        print(f"This is your message in Morse Code: {morse_message}")

    else:
        user_morse_code = input("Enter the Morse code you want converted: ")
        readable_morse = decode_morse(user_morse_code)
        print(f"This is the decoded message: {readable_morse}")

    end_program = input("Would you like to continue? Type Y or N: ").lower()
    if end_program == "n":
        print("Thank you for using the Morse Decoder!")
        program_on = False
