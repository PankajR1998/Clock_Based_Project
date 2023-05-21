from datetime import datetime
from playsound import playsound
import emoji

set_time = input("Set the alarm Time in 'HH:MM:SS'\n")
alarm_hour = set_time[0:2]
alarm_min = set_time[3:5]
alarm_second = set_time[6:8]
alarm_period = set_time[8:10].upper()


while True:
    now = datetime.now()
    current_hour = now.strftime('%I')
    current_min = now.strftime('%M')
    current_second = now.strftime('%S')
    current_period = now.strftime('%p')

    if current_period==alarm_period:
        if current_hour==alarm_hour:
            if current_min== alarm_min:
                if current_second == alarm_second:
                    print('Wake up and have a nice morning!!!'+emoji.emojize(':alarm_clock:'))
                    playsound('wake_up.mp3')
                    break


    