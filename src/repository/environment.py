from repository import project
import os

ENV_URL = r"https://drive.google.com/file/d/1lLzGwu0cBXfJ2EP7FO5io9d4-DvLanLY/view?usp=sharing"
ENV_FOLDER_NAME = "genai_env"
ZIP_ENV_NAME = "genai_env.zip"

def getEnvURL():
    # Return environment zip file's URL. 
    return ENV_URL

def getEnvFolderPath():
    # Get main folder name.
    main_folder_path = project.getFolderPath()

    # Build 'genainev' folder path.
    env_folder_path = os.path.join(main_folder_path, ENV_FOLDER_NAME)

    # check if folder exists:
    if os.path.exists(env_folder_path) == False:
        # Create 'output' folder
        os.mkdir(env_folder_path)

    # Return 'genaienv' folder path
    return env_folder_path

def getZIPEnvPath():
    # Get environment folder path.
    env_folder_path = project.getFolderPath()

    # Build .zip env file path.
    zip_env_path = os.path.join(env_folder_path, ZIP_ENV_NAME)

    # Return .zip environment file path.
    return zip_env_path