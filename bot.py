from instagrapi import Client
from instagrapi.exceptions import LoginRequired

# Replace with your credentials
username = "nihaaal.24"
password = "nihalnik96/"

client = Client()

try:
    client.login(username, password)
except LoginRequired as e:
    print(f"Login failed: {e}")
    exit(1)

def handle_message(message):
    try:
        sender = message.sender_id
        if message.text.lower() == "hi":
            client.send_message(sender, "Hi")
    except Exception as e:
        print(f"Error handling message: {e}")

# Ensure the library has the necessary method for handling messages
# The instagrapi library does not have built-in real-time message handling.
# This is a placeholder for where you might handle messages if such functionality is available.

print("Bot is running. Awaiting messages...")
# Polling for new messages might be needed here if real-time handling is not available.
