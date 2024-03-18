# Example 1
# while True:
#     print("Stuck in an infinite loop.")

# counter = 5
# while counter > 2:
#     print(counter)
#     counter -= 1

# # Example 1
# word = "Python"
# for letter in word:
#     print(letter, end="*")

# text = "OpenEDG Python Institute"
# for letter in text:
#     if letter == "P":
#         break
#     print(letter, end="")
#

#
# text = "pyxpyxpyx"
# for letter in text:
#     if letter == "x":
#         continue
#     print(letter, end="")

# n = 0
#
# while n != 3:
#     print(n)
#     n += 1
# else:
#     print(n, "else")
#
# #print()
#
# for i in range(0, 4):
#     print(i)
# else:
#     print(i, "else")

#
# for i in range(3):
#     print(i, end=" ")  # Outputs: 0 1 2
#
# for i in range(6, 1, -2):
#     print(i, end=" ")  # Outputs: 6, 4, 2

# Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
# for i in range(0, 11):
#     if i % 2 != 0:
#         print(i)

# Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x += 1

# Create a program with a for loop and a break statement. The program should
# iterate over characters in an email address, exit the loop when it reaches the @ symbol,
# and print the part before @ on one line. Use the skeleton below:

# for ch in "john.smith@pythoninstitue.org":
#     if ch == "@":
#         break
#     print(ch, end="")


# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")

# for i in range(0, 6, 3):
#     print(i)


# lst = [1, [2, 3], 4]
# print(lst[1])
# print(len(lst))

# # bubble sort
#
# my_list = [8, 10, 6, 2, 4]  # list to sort
# swapped = True  # It's a little fake, we need it to enter the while loop.
#
# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print(my_list)

# Bubble sort with inputs from users

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)
