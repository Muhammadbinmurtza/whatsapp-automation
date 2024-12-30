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
from datetime import datetime, timedelta
import time

# Twilio credentials
account_sid = "{tamilo acount id }"
auth_token = "{tamilo account token }"
client = Client(account_sid, auth_token)


# define send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_="whatsapp:{number }",
            body=message_body,
            to=f"whatsapp:{recipient_number}"
        )
        print(f"Message sent successfully. Message SID: {message.sid}")
    except twilio.rest.TwilioRestException as e:
        print(f"An error occurred while sending the message: {e}")


# user input
name = input("Enter the name of the recipient: ")
recipient_number = input("Enter the recipient's WhatsApp number with country code: ")
message_body = input(f"Enter the message you want to send to {name}: ")

# Step 5: Parse date/time and calculate delay
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM) 24-hour format: ')

# DATETIME
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# Calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = float(time_difference.total_seconds())

if delay_seconds <= 0:
    print("The time you entered was in the past. Please enter a future time.")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}")

    # Wait until the scheduled time
    time.sleep(delay_seconds)

    # Send the message
    send_whatsapp_message(recipient_number, message_body)