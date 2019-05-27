#  30.	Write a Python program to count the number occurrence of a specific character in a string

string = input('Enter any word:  ')
word = input('Enter the character that you want to count in that word:  ')
lenght = len(string)

count = 0

for i in range(lenght):
    if string[i] == word:
        count = count + 1

print(count)