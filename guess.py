#Guessing Number game in Python

import random

guessesTaken = 0
print ('Hello! what is your name? ')
myName = input()

number = random.randint(1 , 20)
print('Well ' + myName + 'I am thinking of a number from 1 to 20')

for guessesTaken in range(6):
    print('Take a guess?')
    guess = input()
    guess = int(guess)
    
    if guess < number:
        print('You guessedn it to low')

    if guess > number:
        print('You guessed it too high')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good Job ' +  myName + '! You have guessed the number in ' +  guessesTaken + ' guesses')

if guess !=number:
    number = str(number)
    print('Nope, the number I was guessing was' + number + '.')
    