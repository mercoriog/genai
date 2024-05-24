from repository import comfyui as comfylib
import os

# URL filename.
URL_FILE = "comfyURL.txt"

def getURLfilePath():
    # Get 'comfyui' folder path
    comfyui_folder_path = comfylib.getFolderPath()

    # Build user_url file path.
    url_file_path = os.path.join(comfyui_folder_path, URL_FILE)

    # Return url file path.
    return url_file_path

def getURL():
    # Set an exception handler:
    try:
        url_file_path = getURLfilePath()

        # Open user url .txt file
        with open(url_file_path, "r") as file:
            # Read url
            URL = file.read()

        # Return ComfyUI API URL.
        return URL

    # An error occurs:
    except Exception as e:
        # Print the exception.
        print("[ERROR] " + str(e))

        return ""
    

def saveNewURL(URL):
    # Set an exception handler:
    try:
        url_file_path = getURLfilePath()

        # Create user url .txt file
        with open(url_file_path, "w") as file:
            file.write(URL)

        return True

    # An error occurs:
    except Exception as e:
        # Print the exception.
        print("[ERROR] " + str(e))

        return False
