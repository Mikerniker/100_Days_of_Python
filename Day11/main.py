from art import logo
from replit import clear
import random

print(logo)

def blackjack():
  play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  
  player_cards = []
  computer_cards = []
  cards =  [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   #Detect when computer or user has a blackjack.
  def ace_number():
    if cards[0] in player_cards or computer_cards:
      if sum(computer_cards) > 21 and sum(player_cards) > 21:
        cards[0] = 1
      elif sum(computer_cards) > 21 or sum(player_cards) > 21:
        cards[0] = 1
        
  for card in range(2):
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    totalplayer = sum(player_cards)
    totalcomputer = sum(computer_cards)
    ace_number()
  print(f"Your cards: {player_cards}, current score: {totalplayer}")
  print(f"Computer's first card: {computer_cards[0]}") #, current score: {totalcomputer}
  
  play_game = True
  while play_game:
    another_card = input("Type 'y' to get another card, type 'n'to pass: ")
    if another_card == "y":
      player_cards.append(random.choice(cards))
      totalplayer = sum(player_cards)
      print(f"Your cards: {player_cards}, current score: {totalplayer}")
      print(f"Computer's first card: {computer_cards[0]}, current score: {totalcomputer}")
    else: 
      while totalcomputer < 16:
        computer_cards.append(random.choice(cards))
        totalcomputer = sum(computer_cards)
      print(f"Your final hand: {player_cards}, final score: {totalplayer}.")
      print(f"Computer's final hand: {computer_cards}, final score: {totalcomputer}")
      play_game = False
  
  if totalcomputer == 21 and totalplayer == 21:
    print("Computer wins!")
    play_game = False
  elif totalcomputer == 21:
    print("Computer wins!")
    play_game = False
  elif totalplayer == 21:
    print("You win!")
    play_game = False
  elif totalcomputer > 21:
    print("You win!")
    play_game = False
  elif totalplayer > 21:
    print("Computer wins!")
    play_game = False
  elif totalcomputer > totalplayer or totalplayer > 21:
    print("Computer wins!")
  elif totalcomputer < totalplayer:
    print("You win!")
  elif totalcomputer == totalplayer:
    print("It's a draw!")
      
  playagain = input("Would you like to play again? Type 'yes' or 'no'").lower()
  if playagain == "no":
      play_game = False
  elif playagain == "yes":
      clear()
      blackjack()

blackjack()
