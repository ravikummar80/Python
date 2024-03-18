# # Python program to print greater or two numbers
#
# number1 = (int(input("Enter your first number: ")))
# number2 = (int(input(" Enter your second number: ")))
#
# if number1 > number2:
#     larger_number = number1
#     print("The larger number is: ", + larger_number)
# elif number2 > number1:
#     larger_number = number2
#     print("The larger number is: ", + larger_number)
# else:
#     print("Both the numbers are equal")

# Program to print the largest of the three numbers

number1 = (float(input("Enter your first number: ")))
number2 = (float(input("Enter your second number: ")))
number3 = (float(input("Enter your third number: ")))

largest_number = max(number1, number2, number3)

print("The largest number is: ", + largest_number)
