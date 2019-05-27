#  36.	Write a program to check whether given input is palindrome or not

word = input('Please enter a word:  ')

if word[::-1] == word:
    print('This word is a Palindrome.')
else:
    print('This word is not a Palindrome.')