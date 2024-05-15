from repository import source as src
import os 

COMFYUI_FOLDER_NAME = "comfyui"

def getFolderPath():
	# Get 'src' folder path.
	src_folder_path = src.getFolderPath()

	# Build 'comfyui' folder path.
	comfyui_folder_path = os.path.join(src_folder_path, COMFYUI_FOLDER_NAME)

	# Return 'comfyui' folder path.
	return comfyui_folder_path