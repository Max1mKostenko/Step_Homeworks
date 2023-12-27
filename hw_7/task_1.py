str_ = input("Please enter any sentence or word to check if it's a palindrome: ")

if str_.lower() == str_[::-1].lower():
    print("Palindrome!")
else:
    print("Not palindrome!")
