# Alarm Clock🔥

An alarm clock is a clock with a function that can be activated to ring at a time set in advance, used to wake someone up. Here a Python program to create an alarm clock with Python.

## 📌How to Create an Alarm Clock with Python?

As the title suggests, our task here is to write a python script that creates an alarm clock. For this task, I will be using the DateTime, OS, Time module in Python to create an alarm clock.

The DateTime and OS module comes pre-installed in the Python programming language so you can easily import it in your program. Now let’s see how to write a program to create an alarm with Python.

## 📌Alarm Clock with Python

Before writing the program you should know that you also need an alarm tone which will ring at the time of the alarm. So you can download any alarm tune or you can use simple your music gallary songs. Now as we are ready with the libraries and the alarm song, let’s see how to write a program to create an alarm clock with Python:

### Code:

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
            

The user input should be in a format of hours: minutes: and then seconds. You will start listening to the song as you will reach the time that has been set. To test your code set the time 2 or 3 minutes later from the time you are giving the user input. 

## 📌Summary
This idea can be implemented in software applications also, so you now have an idea of what can be a good Python project other than just designing the User interface of an application.
