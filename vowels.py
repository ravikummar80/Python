# Program to print vowels in assending order

def main():
    user_word = input("Enter a word: ")
    user_word = user_word.upper()

    for letter in user_word:
        if letter in "AEIOU":
            continue
        print(letter)

if __name__ == "__main__":
    main()