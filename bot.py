from InstagramAPI import InstagramAPI
import requests
import time
import os

def download_media(media_url, media_type):
    media_path = "temp_media"
    if media_type == "photo":
        media_path += ".jpg"
    elif media_type == "video":
        media_path += ".mp4"

    response = requests.get(media_url, stream=True)
    if response.status_code == 200:
        with open(media_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return media_path
    else:
        raise Exception("Failed to download media")

def send_media(api, user_id, media_path, media_type):
    try:
        if media_type == "photo":
            api.uploadPhoto(media_path)
        elif media_type == "video":
            api.uploadVideo(media_path)
        api.direct_message("Here is the media you requested!", [user_id])
    except Exception as e:
        print(f"Failed to send media: {e}")
    finally:
        os.remove(media_path)  # Clean up by removing the temporary file

def get_media_info(api, shortcode):
    try:
        api.getMediaInfo(shortcode)
        media_info = api.LastJson
        if media_info['items']:
            item = media_info['items'][0]
            if 'video_versions' in item:
                return item['video_versions'][0]['url'], "video"
            elif 'image_versions2' in item:
                return item['image_versions2']['candidates'][0]['url'], "photo"
    except Exception as e:
        print(f"Error fetching media info: {e}")
    return None, None

def main():
    # Hardcoded credentials
    username = "nih4l.23"
    password = "434290"

    api = InstagramAPI(username, password)
    api.login()

    while True:
        try:
            api.getv2Inbox()
            messages = api.LastJson['inbox']['threads']
            for thread in messages:
                for item in thread['items']:
                    if item['item_type'] == 'link':
                        link_text = item['link']['text']
                        user_id = item['user_id']
                        if "instagram.com/p/" in link_text or "instagram.com/reel/" in link_text:
                            shortcode = link_text.split("/")[-2]
                            media_url, media_type = get_media_info(api, shortcode)
                            if media_url:
                                media_path = download_media(media_url, media_type)
                                send_media(api, user_id, media_path, media_type)
                            else:
                                print("Could not fetch media information.")
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()
