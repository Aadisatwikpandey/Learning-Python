import pywhatkit as kit
import time

# Set the phone number (with the country code) and the message
phone_number = "+918707257270"  # Replace with the recipient's phone number
message = "Hello, this is an automated message from Python!"
num_messages = 50  # Number of times to send the message

# Open WhatsApp Web in the default browser


# Wait for a few seconds for WhatsApp Web to load
time.sleep(10)  # Adjust this delay based on your internet speed and computer performance


for _ in range(num_messages):
    kit.sendwhatmsg_instantly(phone_number, message, 5, 2)  # Send the message
    time.sleep(2)  # Delay for 2 seconds between messages
    


