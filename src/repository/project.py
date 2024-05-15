import os

MAIN_FOLDER_NAME = "genai"

def getFolderPath():
	# Project tree is 'genai/src/repository/project.py'.

    # Get root path of this file 'project.py'.
    # So <ROOT_PATH> is the path to 'repository' folder.
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

    # Get main folder path going back to 'genai' folder.
    main_folder_path = os.path.join(ROOT_PATH, "..", "..")
    
    # Return main folder path.
    return main_folder_path