from instabot import Bot
import time

# Create a bot instance
bot = Bot()

# Login to your Instagram account
bot.login(username="nihaaal.24", password="nihalnik96/")

def handle_messages():
    while True:
        try:
            # Fetch all messages
            messages = bot.get_messages()

            for message in messages:
                # Check if the message contains "Halo Guys"
                if "Hi" in message['text']:
                    # Send a reply with "Hi"
                    bot.send_message("Hi", message['user_id'])
                    print(f"Replied to {message['user_id']} with 'Halo'")

            # Sleep to avoid hitting rate limits too quickly
            time.sleep(60)  # Adjust as needed

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(300)  # Wait longer if an error occurs

# Run the message handling function
handle_messages()
