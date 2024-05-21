from repository import comfyui as comfylib
import os
import time

# Output folder path of ComfyUI in local machine.
OUTPUT_DIR = "replace with comfyui ouput directory path"

def getOutputFolderPath():
    # Return output folder path.
    return OUTPUT_DIR

def getLatestImage(folder):
    # This function check for the latest image stored in input folder.

    # Retrive all files in folder.
    files = os.listdir(folder)
    
    # Filter image format file.
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    # Sort images from time.
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)))
    
    # Get latest image as last item in <image_files> list.
    latest_image = os.path.join(folder, image_files[-1]) if image_files else None
    
    # Return latest image of input folder.
    return latest_image
