#  21.	Write a Python program to convert seconds to day, hour, minutes and seconds.

time = float(input("enter the time in seconds: "))
day = time / (24 * 3600)
time = time % (24 * 3600)
hour = time / 3600
time = time % 3600
minutes = time / 60
time = time % 60
seconds = time
print("Day: "+str(day)+"\nHour: "+str(hour)+"\nMinutes: "+str(minutes)+"\nSeconds: "+str(seconds))
