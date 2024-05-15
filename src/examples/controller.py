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

	for preview in preview_images:
		if preview == image_name:
			preview_path = os.path.join(preview_folder_path, preview)
			return preview_path

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
			
			ex_gender = ex.findtext("gender")
			ex_hair_color = ex.findtext("hair-color")
			ex_eyes_color = ex.findtext("eyes-color")
			ex_positive_prompt = ex.findtext("positive-prompt")
			ex_negative_prompt = ex.findtext("negative-prompt")

			# Load the actual image.
			ex_img = Image.open(ex_img_url)

			# Add loaded example to list.
			examples_list.append([
				ex_img,
				ex_gender,
				ex_hair_color,
				ex_eyes_color,
				ex_positive_prompt,
				ex_negative_prompt
			])
	# An error occurs:
	except Exception as e:
		# Print the exception.
		print("[ERROR] " + str(e))

	# Return an empty list if any error occurs.
	return examples_list

