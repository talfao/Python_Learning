from datetime import datetime
#from playsound import playsound

def validate_time(alarm_time):
    if len(alarm_time) != 11 :
        return "Invalid time format! Please try again and never give up!"
    else:
        if int(alarm_time[0:2]) > 12 :
            return "Invalid hour format! Please try again and never give up!"
        elif int(alarm_time[3:5]) > 59 :
            return "Invalid minute format! Please try again and never give up!"
        elif int(alarm_time[6:8]) > 59 :
            return "Invalid second format! Please try again and never give up!"
        else:
            return "ok"

while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
    validate = validate_time(alarm_time.upper())

    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = (alarm_time[9:]).upper()

while True:
    now = datetime.now()

    current_hour = now.strftime("%I")
    current_minute= now.strftime("%M")
    current_second = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_second == current_second:
                    print("please wake up")
                    #playsound("") 
                    break
