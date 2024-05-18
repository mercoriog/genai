from repository import environment as envlib
from service import downloader as down
import os

def loadEnv():
    # This function download the environment from web and store it in env folder.
    # Get path where to store the ZIP env file.  
    zip_env_path = envlib.getZIPEnvPath()
    
    # Get ZIP env URL.
    zip_env_URL = envlib.getEnvURL()
    
    # Download ZIP env file and unzip to get it ready to use.
    # Set 'delete_when_unzipped=True' param to delete ZIP file after unzip operation.
    env = down.downloadAndUnzip(zip_env_URL, zip_env_path, True)

    # This function returns True if env folder is loaded.
    # If any error occurs, <env> value is False.
    return env


def checkEnv():
    # This function checks if environment is loaded.
    # Get environment folder path.
    env_folder_path = envlib.getEnvFolderPath()

    # List all env folder files.
    env_folder_files = os.listdir(env_folder_path)

    # If env folder is empty:
    if len(env_folder_files) == 0:
        # Return False.
        return False

    # This function returns True if env folder is not empty.
    return True

def initEnv():
    # This function check if environment is loaded: 
    # if not loaded, it download the .zip file from web,
    # unzip it and stores the environment in correct folder.
    
    # Check if env is loaded.
    env = checkEnv()

    # If env is not loaded:
    if not env:
        # Notify env not loaded.
        print("[ENV] Environment NOT loaded.")

        env = loadEnv()

        # Check if env loading is done:
        if env == True:
            # Notify initialization done.
            print("[ENV] Environment loaded with no errors.")

    # This function returns True if environment is loaded.
    # If any error occurs, <env> value is False.
    return env
