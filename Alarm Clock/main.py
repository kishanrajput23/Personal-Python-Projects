import os
import datetime
import time

year, month, day = input("Enter the date = ").split("/")    #splitting input values by'/'

hour, minutes, second = input("Enter the Time = ").split(":")    #splitting input values by':'

shedule_date = datetime.date(int(day), int(month), int(year))    #converting input values into interger

n = 1

while n > 0:
    
    if time.localtime().tm_hour == int(hour) and time.localtime().tm_min == int(minutes) and time.localtime().tm_sec == int(second) and datetime.date.today() == shedule_date:
        
        os.startfile("C:\\Users\\KISHAN\\Music\\Chogada.mp3")    #Enter the path of a song or ringtone where it is placed in your system
        
        break
    
    else:
        
        n +=1
