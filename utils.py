import os
import time

def cleanup_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def wait(seconds):
    time.sleep(seconds)
