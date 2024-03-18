# # This is a Python program to take integer and prints
#
# n = int(input("Enter an Integer: "))
# print(n >= 100)

# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)


# counter = 5
# while counter:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

# numbers = [10, 5, 7, 2, 1]
# print("Original list content:", numbers)  # Printing original list content.
#
# numbers[0] = 111
# print("New list content: ", numbers)  # Current list content.

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)
