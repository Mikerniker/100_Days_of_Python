print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')



print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


direction = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n')

if direction.lower() == "right":
  print("You were attacked and eaten by a wild dingo. Game Over.")
elif direction.lower() == "left":
  lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
  if lake.lower() == "swim":
    print("You get captivated by the songs of sirens and lured down to the lake and drown. Game Over.")
  else:
    doors = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
    if doors.lower() == "blue":
      print("You enter a room of of puppies. You are immobilized by cuteness. You win their love, but lose the treasure. Game Over.")
    elif doors.lower() == "yellow":
      print("You found the treasure! You Win!")
    elif doors.lower() == "red":
      print("You enter a room full of doors to other rooms and cannot escape. Game Over.")
    else: 
      print("You chose a door that doesn't exist. Game Over.")
