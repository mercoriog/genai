from repository import examples as exlib

EXAMPLES_XML = "examples.xml"

def getExamplesFilePath():
	# Get 'examples' folder path.
	examples_folder = exlib.getFolderPath()
	
	# Build examples.xml file path.
	examples_file_path = os.path.join(examples_folder, EXAMPLES_XML)
	
	# Return examples.xml file path.
	return examples_file_path

