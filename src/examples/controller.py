from PIL import Image
from examples import repository as repo
from repository import preview as prev
import xml.etree.ElementTree as ET
import os

def getExImagePath(image_name):
	# Get 'preview' folder path.
	preview_folder_path = prev.getFolderPath()

	# List all images in preview folder.
	preview_images = os.listdir(preview_folder_path)

	# For each basename from folder path: 
	for preview_basename in preview_images:
		
		# Check if basename is equal target image name.
		if preview_basename == image_name:
			
			# Target image file found. Get the correct path.
			preview_file_path = os.path.join(preview_folder_path, preview_basename)
			
			# Return absolute path of target image file (founded in 'preview' folder)
			return preview_file_path

	return ""

def getExamples():
	# Get examples.xml file.
	example_xml_file = repo.getExamplesFilePath()

	# Create an empty examples list.
	examples_list = []

	# Set exception handler:
	try:
		# Parse the xml file to get the entire tree structure.
		ex_tree = ET.parse(example_xml_file)

		# Get the root of xml file tree.
		ex_root = ex_tree.getroot()

		# Scroll the entire tree:
		for ex in ex_root.findall("example"):
			# Retrive every subelement.
			ex_img_name = ex.findtext("image-name")
			
			# Retrive url from image name.
			ex_img_url = getExImagePath(ex_img_name)
			
			# Retrive positive prompt text.
			ex_positive_prompt = ex.findtext("positive-prompt")
			
			# Retrive negative prompt text.
			ex_negative_prompt = ex.findtext("negative-prompt")

			# Load the actual image.
			ex_img = Image.open(ex_img_url)

			# Add loaded example to list.
			examples_list.append([
				ex_img,
				ex_positive_prompt,
				ex_negative_prompt
			])
	# An error occurs:
	except Exception as e:
		# Print the exception.
		print("[ERROR] " + str(e))

	# Return an empty list if any error occurs.
	return examples_list

