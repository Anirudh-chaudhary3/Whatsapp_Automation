""" 
1 - Twilio client setup
2 - User Inputs
3 - Scheduling Logic
4 - Send Message
"""

# STEP - 1 : Installed Required Libraries
from twilio.rest import Client
from datetime import datetime , timedelta
import time

# STEP - 2 : Twilio Credentials
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# STEP - 3 : Define Send Message Function

def send_message_function(recepient_number , message_body):
    try:
        message = client.messages.create(   
            from_='whatsapp:',
            body=message_body,
            to=f'whatsapp:+91{recepient_number}'  
        )
        print(f"Message Send Successfully !!! Message SID{message.sid}")
    except Exception as e:
        print("An Error Occurred")

# STEP - 4 : User Inputs
name = input("Enter the Recepient Name :")
recepient_number = input("Enter the Recepient Whatsapp Number with Country Code. eg(+91 for India) :")
message_body = input(f"Enter the Message you want to send to {name} :")

# STEP - 5 : Parse Date/Time and Calculate Delay
date_str = input("Enter the Date to send the Message (YYYY-MM-DD) :")
time_str = input("Enter the Time to send Message (HH:MM in 24 Hours Format) :")

# DateTime
scheduled_datetime = datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# Calculate Delay
time_difference = scheduled_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("The Specified time is in the Past !!!. Please Enter a Future Date and Time...")
else:
    print(f"Message scheduled to be sent to {name} at {scheduled_datetime}.")

    # wait until the scheduled time
    time.sleep(delay_seconds)

    # send the message
    send_message_function(recepient_number , message_body)