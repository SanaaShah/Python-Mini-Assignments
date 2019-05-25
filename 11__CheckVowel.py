#  11.	Write a Python program to test whether a passed letter is a vowel or not

letter = input('Please enter any letter:   ')

if letter == 'a' or letter == 'e' or letter == 'o' or letter == 'u' or letter == 'i' \
   or letter == 'A' or letter == 'E' or letter == 'O' or letter == 'U' or letter == 'I':
    print('Entered letter is a vowel.')
else:
    print('Its not a vowel.')