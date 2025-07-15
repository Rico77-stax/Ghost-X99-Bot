# utils.py

import os
import requests
from datetime import datetime

def download_image(file_url, bot_token):
    try:
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = f"screenshots/chart_{now}.jpg"
        
        response = requests.get(file_url)
        if response.status_code == 200:
            os.makedirs("screenshots", exist_ok=True)
            with open(file_path, "wb") as f:
                f.write(response.content)
            return file_path
        else:
            print(f"Failed to download image: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None
