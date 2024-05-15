from repository import main
import os 

SOURCE_FOLDER_NAME = "src"

def getFolderPath():
	# Get 'main' folder path.
	main_folder_path = main.getFolderPath()

	# Build 'src' folder path.
	src_folder_path = os.path.join(main_folder_path, SOURCE_FOLDER_NAME)

	# Return 'src' folder path.
	return src_folder_path