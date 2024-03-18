# Python program to check character case and respond

# input_str = input("Enter a plant name: ")
#
# if input_str == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant! ever")
# elif input_str == "spathiphyllum":
#     print("No - I want a bigger Spathiphyllum")
# else:
#     print("Spathiphyllum! Not", input_str + "!")
#
# print(input_str)


# Program using while loop to validate user input and terminate on input matching chupacabra


secret_word = "chupacabra"

while True:
    user_input = input("Enter a word: ")
    if user_input == secret_word:
        print("You have successfully left the loop")
        break
