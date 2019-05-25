#  20.	Write a Python program to convert all units of time into seconds.

days = int(input("Enter the days: ")) * 3600 * 24
hours = int(input("Enter the hours: ")) * 3600
minutes = int(input("Enter the minutes: ")) * 60
seconds = int(input("Enter the seconds: "))

total_time = days + hours + minutes + seconds

print("The  amounts of seconds:  "+str(total_time))
