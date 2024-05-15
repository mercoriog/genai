from repository import project
import os 

SOURCE_FOLDER_NAME = "src"

def getFolderPath():
	# Get 'main' folder path.
	main_folder_path = project.getFolderPath()

	# Build 'src' folder path.
	src_folder_path = os.path.join(main_folder_path, SOURCE_FOLDER_NAME)

	# Return 'src' folder path.
	return src_folder_path