from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Twilio credentials
account_sid = "{tamilo account id }"
auth_token = "{tamilo account token }"
client = Client(account_sid, auth_token)

# Define send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:{number}',
            body=message_body,
            to=f'whatsapp:+{recipient_number}'
        )
        print(f"Message sent successfully. Message SID: {message.sid}")
    except Exception as e:
        print(f"Error sending message: {e}")

# User input
name = input("Enter the name of the recipient: ")
recipient_number = input("Enter the WhatsApp number of the recipient with country code: ")
message_body = input(f"Enter the message you want to send to {name}: ")

# Parse date/time and calculate delay
date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM) in 24-hour format: ")

try:
    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
    current_datetime = datetime.now()
    time_difference = schedule_datetime - current_datetime
    delay_seconds = time_difference.total_seconds()

    if delay_seconds <= 0:
        print("The time you entered is in the past. Please enter a future time.")
    else:
        print(f"Message scheduled to be sent to {name} at {schedule_datetime}.")
        time.sleep(delay_seconds)
        send_whatsapp_message(recipient_number, message_body)
except ValueError as e:
    print(f"Invalid date or time format: {e}")
