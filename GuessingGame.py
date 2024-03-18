# This is a Guess the number game
# Date : 30-7-2022

import random
guessessTaken = 0

print("Hello! what is your name?")
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 to 20')

for guessessTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low')

    if guess > number:
        print('Your guess is too high')

    if guess == number:
        break
if guess == number:
    guessessTaken = str(guessessTaken + 1)
    print('Good Job! ', myName + '! you guessed my number in ' + guessessTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
