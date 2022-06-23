import os
from anyio import current_time
from playsound import playsound
import datetime

extracted_time = open('D:\\MARTHA\\data.txt','rt')
time = extracted_time.read()
Time = str(time)

delete_time = open('D:\\MARTHA\\data.txt','r+')
delete_time.truncate(0)
delete_time.close()

def ringerNow(time):
    time_to_set = str(time)
    time_now = time_to_set.replace("martha","")
    time_now = time_to_set.replace("set alarm for","")
    time_now = time_to_set.replace(" and ",":")

    alarm_time = str(time_now)

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")

        if current_time == alarm_time:
            print("Wake Up Sir, It's time to work.......")
            speak("Wake Up Sir, It's time to work.......")

        elif current_time > alarm_time:
            break
