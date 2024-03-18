import random
def play_game():
	number_to_guess = random.randint(1, 20)
	attempts = 0

	while attempts < 5:
		guess = int(input("Guess a number between 1 and 20: "))

		if guess < number_to_guess:
			print("Too Low!")
		elif guess > number_to_guess:
			print("Too High!")
		else:
			print('Congratulations! You guessed the number!', + int(guess) + 'guesses')
			break

	attempts += 1
	
	if attempts == 5:
		print("Sorry, you  reached the maximum number of attempts. The number was", number_to_guess)

	play_again = input("Do you want to play again? (Yes/No): ")

	if play_again.lower() == "yes":
		play_game()
	else:
		print("Thank you for playing!")

play_game()

	