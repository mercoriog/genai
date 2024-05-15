from repository import project
import os 

MEDIA_FOLDER = "media"

def getFolderPath():
	# Get 'main' folder path.
	main_folder_path = project.getFolderPath()

	# Build 'media' folder path.
	media_folder_path = os.path.join(main_folder_path, MEDIA_FOLDER)

	# Check if 'media' folder exists:
	if os.path.exists(media_folder_path) == False:
		# Create 'media' folder.
		os.mkdir(media_folder_path)

	# Return 'media' folder path.
	return media_folder_path