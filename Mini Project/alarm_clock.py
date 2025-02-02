import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file="alarm"
    isrunning=True
    while isrunning:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("WAKE UP !!!😫🥱")
            pygame.mixer.init()
            #pygame.mixer.music.load(sound_file)
            pygame.mixer.music.load("C:\\Users\\parth\\OneDrive\\Desktop\\parth\\alarm.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            isrunning=False
        time.sleep(1)


alarm_time=input("Set Your alarm:(HH:MM:SS):")
set_alarm(alarm_time)

