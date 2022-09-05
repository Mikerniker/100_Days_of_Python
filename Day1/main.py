#Greeting
welcome = "Welcome to the Band Name Generator"
print(welcome)

#Ask the user where they grew up.
city = input("What's the name of the city you grew up in?\n").capitalize()

#Ask the user for the last thing they ate.
food = input("What's the last thing you ate? \n").capitalize()

#Combine the name of city and food they ate and show the the band name.
print("Your band name could be " + city + " " + food)
