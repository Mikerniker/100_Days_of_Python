from art import logo, vs
from game_data import data
import random
from replit import clear

#GENERATE A RANDOM PERSON
def choices():
    choice = random.choice(data)
    return choice

def game_play():  
  def check_followercount(a, b):
    a_count = a['follower_count']
    b_count = b['follower_count']
    if a_count > b_count:
      return a_count
    elif a_count < b_count:
      return b_count 

  def high_low():
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
#{a['follower_count']
    print(vs)
 
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
#{b['follower_count']}  
    
  play_game = True
  score = 0
  b = choices()
  while play_game:
    print(logo)
    a = b
    b = choices()
    
    high_low()    
    highest_follower = check_followercount(a, b)
    guess = input("Who has more followers, Type 'A' or 'B'? ").lower()
    if guess == 'a':
      guess = a
    elif guess == 'b':
      guess = b
    
    if guess['follower_count'] == highest_follower:
      score += 1
      clear()
      a = guess
      print(f"You're right! Current score: {score}")
      
    else:
      print(f"Sorry, that's wrong. Final score {score}")
      play_game = False

#highest_follower = check_followercount(a, b)    
game_play()

