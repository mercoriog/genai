from gallery import repository as gallib
from PIL import Image
from pathlib import Path

def extractNameNoExt(filename):
    # This function extract the exact name of the file (without extension).
    return Path(filename).stem

def getGalleryNames():
    # Get 'gallery' folder path.
    gallery_folder = gallib.getFolderPath()

    # Create an empty gallery names list.
    gallery_names = []

    # For each image in gallery folder.
    for image in gallery_folder:
        # Extract current gallery's image name.
        name = extractNameNoExt(image)

        # Add to gallery names list.
        gallery_names.append(name)

    # Return a list of gallery's images name.
    return gallery_names

def getGalleryImages():
    # Get 'gallery' folder path.
    gallery_folder = gallib.getFolderPath()

    # For each image in gallery folder.
    for image in gallery_folder:
        # Load image.
        loaded_image = Image.open(image)

        # Add to gallery images list.
        gallery_images.append(loaded_image)

    # Return gallery loaded images list.
	return gallery_images