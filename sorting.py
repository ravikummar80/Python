# Read 5 numbers from the user and print in ascending order

numbers = []
for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# sorting the number in ascending order

numbers.sort()

print("Numbers in ascending order: ")
for num in numbers:
    print(num)

