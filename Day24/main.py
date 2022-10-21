with open("./Input/Letters/starting_letter.txt") as let:
    letter = let.read()
    print(letter)

with open("./Input/Names/invited_names.txt") as file:
    # contents = file.read()
    names = file.readlines()

for name in names:
    new = name.strip("\n")
    with open(f"./Output/ReadyToSend/letter_for_{new}.txt", mode="w") as final:
        final.write(letter.replace("[name]", new))
