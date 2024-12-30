"""
twilio
datetime module
time module
"""
"""
1- twilio client setup
2- user input
3- scheduling logic
4- sending the message
"""

from twilio.rest import Client
from datetime import datetime , timedelta
import time

# Twilio credentials


account_sid = "{tamilo acount id }"
auth_token = "{tamilo account token }"
client = Client(account_sid, auth_token)

# define send message function

def send_whataspp_message(recipient_number , message_body):
    try:
        message = client.messages.create(
            from_= 'whatsapp : +{number}',
            body= message_body,
            to= f'whatsapp : +{recipient_number}'
        )
        print(f"Message sent successfully. Message SID: {message.sid}")
    except  Exception as e:
        print(f"Error sending message")
 
# user input
name = input("enter the name of the recipient ")
recipient_number = input("enter the number of the recipient whatsapp number with country code ")
message_body = input(f"Enter the message you wanna send to the : {name}")

#step 5 , parse  date/time  and calculate  delay
date_str = input('enter the date to send the message (YYYY-MM-DD):')
time_str = input('enter the time to send the message (HH:MM) 24 hours format: ')
# DATETIME  
schedule_datetime =  datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# calculate delay
time_difference = schedule_datetime - current_datetime 
delay_seconds = float(time_difference.total_seconds())
if  delay_seconds <= 0: 
    print("the time you entered was a past , please enter a future time ") 
else:
    print(f"message scheduled to be sent to {name} at {schedule_datetime} ")

    # wait until the scheduled time 
    time.sleep(delay_seconds)

    # send the message
    send_whataspp_message(recipient_number, message_body)

