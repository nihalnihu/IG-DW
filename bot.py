from flask import Flask, request, jsonify
from instagrapi import Client
import threading
from PIL import Image
import time

# Initialize the Flask app
app = Flask(__name__)

# Initialize Instagrapi Client
client = Client()

# Login to Instagram account
client.login(username="nihaaal.24", password="nihalnik96/")

# Function to handle messages
def handle_messages():
    while True:
        try:
            # Fetch messages
            messages = client.direct_threads()  # This may need adjustment based on instagrapi's API

            for thread in messages:
                for message in thread['messages']:
                    if "Halo" in message['text']:
                        # Send a reply with "Hi"
                        client.direct_send("Hi", thread['users'])
                        print(f"Replied to {thread['users']} with 'Hi'")

            time.sleep(60)  # Adjust the sleep time as needed
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(300)  # Wait longer if an error occurs

# Flask route to start message handling
@app.route('/start', methods=['POST'])
def start_handling_messages():
    # Start message handling in a separate thread
    thread = threading.Thread(target=handle_messages)
    thread.start()
    return jsonify({"status": "Message handling started"}), 200

# Flask route to stop message handling
@app.route('/stop', methods=['POST'])
def stop_handling_messages():
    # Implement a mechanism to stop the message handling (e.g., setting a flag)
    return jsonify({"status": "Message handling stopped (not implemented)"}), 200

# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
