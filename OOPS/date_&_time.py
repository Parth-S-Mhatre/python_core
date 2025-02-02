import datetime
date=datetime.date(2024,2,7) # year-month-day
print(date)
time=datetime.time(12,30,0)
print(time)
today=datetime.date.today()
print(f"todays date= {today}")
now=datetime.datetime.now()
print(f"todays date and timing = {now}") 

target_date=datetime.datetime(2020,1,2,12,30,0)
cuurent_date=datetime.datetime.now()

if target_date<cuurent_date:
    print("target has passed")
else:
    print("Target has not pass")



import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file="alarm.mp3"
    isrunning=True
    while isrunning:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("WAKE UP !!!😫🥱")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            isrunning=False
        time.sleep(1)


alarm_time=input("Set Your alarm:(HH:MM:SS):")
set_alarm(alarm_time)

