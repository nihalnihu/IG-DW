from instagrapi import Client

# Replace with your credentials 
# nihaaal.24 nihalnik96/
username = "nihaaal.24"
password = "nihalnik96/"

client = Client()
client.login(username, password)

def handle_message(message):
    sender = message.sender_id
    if message.text.lower() == "hallo":
        client.send_message(sender, "Hi")

# Assuming the library has a method to listen for messages
client.add_message_handler(handle_message)
client.listen_for_messages()
