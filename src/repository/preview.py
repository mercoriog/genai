from repository import media
import os 

PREVIEW_FOLDER = "preview"

def getFolderPath():
	# Get 'media' folder path.
	media_folder_path = media.getFolderPath()

	# Build 'preview' folder path.
	preview_folder_path = os.path.join(media_folder_path, PREVIEW_FOLDER)

	# Check if 'preview' folder exists:
	if os.path.exists(preview_folder_path) == False:
		# Create 'preview' folder.
		os.mkdir(preview_folder_path)

	# Return 'preview' folder path.
	return preview_folder_path