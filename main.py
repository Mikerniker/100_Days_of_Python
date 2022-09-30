import random
from hangman_words import word_list
from hangman_art import stages, logo
from replit import clear


print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TEST
#print(f'The solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()   
    if guess in display:
      print(f"You've already guessed {guess}.")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
          
    if guess not in chosen_word:
      lives -= 1
      if 3 <= lives <= 5:
        print(f"Eep, you guessed: {guess}, that's not in the word. 😱 You have {lives} chances left before the hangman makes his final judgment.")
      elif 1 <= lives < 3:
        print(f"You guessed: {guess}, that's not in the word. You have {lives} chances left 😢...the hangman is coming!!!")
      elif lives == 0:
        print(f"OOh nooo. The hangman got youu! The answer was: {chosen_word}.😭😭")
        end_of_game = True
        

    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("WOOOOT! You've escaped the hangman's noose! 🥲 YOU WINNN!!!! 🥳")


    print(stages[lives])


