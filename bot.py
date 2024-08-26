from instabot import Bot

# Create a bot instance
bot = Bot()

# Login to your Instagram account
bot.login(username="nihaaal.24", password="nihalnik96/")

# Define a function to respond to messages
def handle_messages():
    # Fetch all messages
    messages = bot.get_messages()

    for message in messages:
        # Check if the message contains "Halo Guys"
        if "Halo Guys" in message['text']:
            # Send a reply with "Hi"
            bot.send_message("Hi", message['user_id'])

# Run the message handling function
handle_messages()
