def palindromo ():
    if str(word) == str(word)[ :: -1]:
        print(f"The word {word} is palindrome")
    else:
        print(f"The word {word} is not palindrome")

word = input("Enter a word to know it is palindrome or not: ")
palindromo()


