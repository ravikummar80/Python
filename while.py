# This program is exam for while loop

# i = 0
# while i < 100:
#     i += 1
# print (i)

# for i in range(100):
#     pass
#     print("The value of i is", i)
#
# for i in range(2, 8):
#     print("The value of i currently is", i)

# for i in range(2, 1):
#     print("The value of i currently is:", i)

# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is:", power)
#     power *=2

# def introduction(first_name, last_name):
#     print("Hello my name is: ", first_name, last_name)
#
# introduction("Sachin", "Tendulkar")
# introduction("Rahul", "Dravid")
# introduction("MS", "Dhoni")

# def introduction(first_name, last_name="Smith"):
#     print("Hello, my name is", first_name, last_name)
#
# introduction("Super")

# def introduction(first_name="John", last_name="Smith"):
#     print("Hello, my name is", first_name, last_name)
#
# introduction()


# def address(street, city, postal_code):
#     print("Your address is:", street, "St.,", city, postal_code)
#
# s = input("Street: ")
# p_c = input("Postal Code: ")
# c = input("City: ")
#
# address(s, c, p_c)


# def happy_new_year(wishes=True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
# happy_new_year()
# print("Happy New Year!")

# def strange_function(n):
#     if(n % 2 == 0):
#         return True
#
# print(strange_function(2))
# print(strange_function(1))

# def list_sum(lst):
#     s = 0
#
#     for elem in lst:
#         s += elem
#
#     return s
#
#
# print(list_sum([5, 4, 3]))

def strange_list_fun(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list


print(strange_list_fun(10))


