import os
import datetime
import time

def get_user_input():
    year, month, day = input("Enter the date (YYYY/MM/DD) = ").split("/")
    hour, minutes, second = input("Enter the Time (HH:MM:SS) = ").split(":")
    
    return int(year), int(month), int(day), int(hour), int(minutes), int(second)

def schedule_notification(year, month, day, hour, minutes, second):
    schedule_date = datetime.date(year, month, day)
    
    while True:
        current_time = time.localtime()
        if (current_time.tm_hour == hour and
            current_time.tm_min == minutes and
            current_time.tm_sec == second and
            datetime.date.today() == schedule_date):
            return True
        time.sleep(1)
    return False

def play_notification():
    os.startfile("C:\\Users\\KISHAN\\Music\\Chogada.mp3")  # User can replace with their file path

if __name__ == "__main__":
    year, month, day, hour, minutes, second = get_user_input()
    
    if schedule_notification(year, month, day, hour, minutes, second):
        play_notification()
