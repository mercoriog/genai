from PIL import Image
import os
import xml.etree.ElementTree as ET

EXAMPLES_XML_PATH = "genai\\src\\gui\\examples\\examples_config.xml"

def getExamples():
	examples_list = []
	ex_tree = ET.parse(EXAMPLES_XML_PATH)
	ex_root = ex_tree.getroot()

	# scroll the entire tree
	for ex in ex_root.findall("example"):
		# retrive every subelement
		ex_img_url = ex.findtext("image-url")
		ex_gender = ex.findtext("gender")
		ex_hair_color = ex.findtext("hair-color")
		ex_eyes_color = ex.findtext("eyes-color")
		ex_positive_prompt = ex.findtext("positive-prompt")
		ex_negative_prompt = ex.findtext("negative-prompt")
		
		# load the actual image
		ex_img = Image.open(ex_img_url)

		# create a list 
		examples_list.append([
			ex_img,
			ex_gender,
			ex_hair_color,
			ex_eyes_color,
			ex_positive_prompt,
			ex_negative_prompt
		])
	return examples_list

def getExamplesInfo():
	return len(examples_list)

def getExampleItem(index):
	return examples_list[index]

