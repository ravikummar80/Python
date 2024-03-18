# # Python program to calculate income tax
#
# income = float(input("Enter the annual income: "))
#
# if income <= 85528:
#     tax = income * 0.18 - 566.02
# else:
#     tax = 14839.02 + (income - 85528) *0.32
# return max( tax, 0)

x = 10

if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")


