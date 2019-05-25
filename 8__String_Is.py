#  8. Write a Python program to get a new string from a given string where
#  "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged

str = input('Please enter any string starting with or without \' Is \':    ')
check = str[:2]
if check == 'Is':
    print(str)
else:
    print('Is'+str)
