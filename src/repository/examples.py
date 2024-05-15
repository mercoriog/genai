from repository import source as src 
import os 

EXAMPLES_FOLDER = "examples"

def getFolderPath():
	# Get 'src' folder path.
	src_folder_path = src.getFolderPath()

	# Build 'examples' folder path.
	examples_folder_path = os.path.join(src_folder_path, EXAMPLES_FOLDER)

	# Return 'examples' folder path.
	return examples_folder_path