from flask import Flask
import random

number_to_guess = random.randint(0, 9)
colors = ["72A0C1", "0048BA", "3B7A57", "007FFF", "2E5894", "54626F", "318CE7", "333399", "126180", "6699CC"]

app = Flask(__name__)

@app.route('/')
def high_low_game():
    return '<h1>Guess a number between 0 and 9</h1> ' \
           '<img src="https://media.giphy.com/media/Rs2QPsshsFI9zeT4Kn/giphy.gif" width=300px>'

@app.route("/<int:number>")
def check_number(number):
    if number < number_to_guess:
        return f"<h1 style='color:#{colors[random.randint(0, len(colors))]}'>{number} is too low!</h1> " \
               f"<img src='https://media.giphy.com/media/XKvNduSwo0nEXsjZAg/giphy.gif' width=300>"
    elif number > number_to_guess:
        return f"<h1 style='color:#{colors[random.randint(0, len(colors))]}'>{number} is too high!</h1> " \
               f"<img src='https://media.giphy.com/media/oZ7zyrQwFaRyM/giphy.gif' width=300>"
    elif number == number_to_guess:
        return f"<h1 style='color:#{colors[random.randint(0, len(colors))]}'>{number} is woofderful!</h1> " \
               f"<img src='https://media.giphy.com/media/pHZdGyFNp5sUXq4jp5/giphy-downsized-large.gif' width=300>"


if __name__ == '__main__':
    app.run(debug=True)
