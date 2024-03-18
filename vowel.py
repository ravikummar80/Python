# This program check for vowel and prints the output

# def vowel_eater():
#     user_word = input("Enter a word: ")
#     user_word = user_word.upper()
#     word_without_vowels = ""
#
#     for letter in user_word:
#         if letter in "AEIOU":
#             continue
#         word_without_vowels += letter
#
#     print("Words without vowels: ", word_without_vowels)
#
# vowel_eater()

# # Sorting
# lst = [5, 3, 1, 2, 4]
# print(lst)
#
# lst.sort()
# print(lst)  # outputs: [1, 2, 3, 4, 5]

# lst = [5, 3, 1, 2, 4]
# print(lst)
#
# lst.reverse()
# print(lst)  # outputs: [4, 2, 1, 3, 5]

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)

#
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:-1]
# print(new_list)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[:3]
# print(new_list)

# def message(number):
#     print("Enter a number:", number)
#
# message(1)


# def message(number):
#     print("Enter a number:", number)
#
# number = 1234
# message(1)
# print(number)

def message(what, number):
    print("Enter",what, "number", number)

message("Telephone", 11)
message("price", 5)
message("number", "number")