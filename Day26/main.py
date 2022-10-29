import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(new_dict)

#Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Type your word: ")
user = list(user_word.upper())
print(user)

nato_list = [new_dict[letter] for letter in user if letter in new_dict]
print(nato_list)
