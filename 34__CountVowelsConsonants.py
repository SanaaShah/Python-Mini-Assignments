#  34.	Input a text and count the occurrences of vowels and consonant

letter = input('Please enter any letter:   ')

count_vowel = 0
count_consonant = 0

for i in range(len(letter)):
    if letter[i] == 'a' or letter[i] == 'e' or letter[i] == 'o' or letter[i] == 'u' or letter[i] == 'i' \
         or letter[i] == 'A' or letter[i] == 'E' or letter[i] == 'O' or letter[i] == 'U' or letter[i] == 'I':
        count_vowel = count_vowel + 1
    else:
         count_consonant = count_consonant + 1

print('The number of consonants is:  ', count_consonant, ' and the number of vowels is:  ', count_vowel)