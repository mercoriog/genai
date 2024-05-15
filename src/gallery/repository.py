from repository import media
import os 

GALLERY_FOLDER = "gallery"

def getFolderPath():
	# Get 'media' folder path.
	media_folder_path = media.getFolderPath()

	# Build 'gallery' folder path.
	gallery_folder_path = os.path.join(media_folder_path, GALLERY_FOLDER)

	# Check if 'gallery' folder exists:
	if os.path.exists(gallery_folder_path) == False:
		# Create 'gallery' folder.
		os.mkdir(gallery_folder_path)

	# Return 'gallery' folder path.
	return gallery_folder_path