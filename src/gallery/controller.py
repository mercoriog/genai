from gallery import repository as gallib
from PIL import Image
from pathlib import Path
import os

def extractNameNoExt(filename):
    # This function extract the exact name of the file (without extension).
    return Path(filename).stem

def getGalleryNames():
    # Get 'gallery' folder path.
    gallery_folder = gallib.getFolderPath()

    # Create an empty gallery names list.
    gallery_names = []

    # List all images in gallery folder.
    preview_files = os.listdir(gallery_folder)
    
    # Filter image format file.
    gallery_images = [f for f in preview_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # For each image in gallery folder.
    for image in gallery_images:
        # Extract current gallery's image name.
        name = extractNameNoExt(image)

        # Add to gallery names list.
        gallery_names.append(name)

    # Return a list of gallery's images name.
    return gallery_names

def getGalleryImages():
    # Get 'gallery' folder path.
    gallery_folder = gallib.getFolderPath()

    # List all images in gallery folder.
    preview_files = os.listdir(gallery_folder)
    
    # Filter image format file.
    gallery_images = [f for f in preview_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Create an empty list for loaded image.
    loaded_list = []

    # For each image in gallery folder.
    for image in gallery_images:
        # Get the correct image path.
        image_path = os.path.join(gallery_folder, image)

        # Load image.
        loaded_image = Image.open(image_path)

        # Add to gallery images list.
        loaded_list.append(loaded_image)
        
    # Return gallery loaded images list.
    return loaded_list

def getOrderedImages():
    garments_list = getGalleryImages()
    garments_name = getGalleryNames()
    ordered_garments = []
    count = 0

    for item in garments_list:
        ordered_garments.append((item, garments_name[count]))
        count += 1
    
    return ordered_garments


def getOrderedGarments():
    garments_list = getGalleryNames()
    ordered_garments = []
    count = 0

    for item in garments_list:
        count += 1
        ordered_garments.append((item, count))
    
    return ordered_garments
