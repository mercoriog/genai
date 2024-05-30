from repository import comfyui as comfylib
import os

PROMPTS_FILE = "comfyPrompts.txt"

def getPromptFilePath():
	# Get comfyui folder path.
	comfyui_folder_path = comfylib.getFolderPath()

	# Build prompts file path.
	prompts_file_path = os.path.join(comfyui_folder_path, PROMPTS_FILE)

	# Return prompts file path.
	return prompts_file_path

def getCurrentPrompts():
	# Set an exception handler:
	try:
		# Get prompts file path.
		prompts_file_path = getPromptFilePath()
		
		# Set a counter.
		counter = 0

		# Set a matrix.
		prompt_matrix = []

		# Set a row.
		prompt_row = []

		# Create the file.
		with open(prompts_file_path, "r") as file:
			# For each line in file.
			for line in file:
				if line == "\n":
					continue
					
				if counter == 0:
					# Read positive prompt index.
					prompt_row.append(int(line))
				
				elif counter == 1:
					# Read negative prompt index.
					prompt_row.append(int(line))

				else:
					# Read seed.
					prompt_row.append(int(line))

				# When row is complete, update matrix and clean row.
				if len(prompt_row) == 3:
					# Update matrix.
					prompt_matrix.append(prompt_row)
					
					# Clean row.
					prompt_row = []

				# Increase counter.
				counter += 1

		# Return true if writing operation is done with no error.
		return prompt_matrix
	# An error occurs:
	except Exception as e:
		# Print the exception.
		print("[ERROR] " + str(e))
		return None

def savePrompts(prompt_matrix):
	# Set an exception handler:
	try:
		# Get prompts file path.
		prompts_file_path = getPromptFilePath()

		# Create the file.
		with open(prompts_file_path, "w") as file:
			# The matrix has three column: 
			# Positive - Negative - Seed
			for row in prompt_matrix:
				# Get Positive index.
				positive = row[0]

				# Write positive prompt index.
				file.write(str(positive) + "\n")

				# Get Negative index.
				negative = row[1]

				# Write negative prompt index.
				file.write(str(negative) + "\n")

				# Get seed index.
				seed = row[2]

				# Write seed.
				file.write(str(seed)+"\n")
		# Return true if writing operation is done with no error.
		return True

	# An error occurs:
	except Exception as e:
		# Print the exception.
		print("[ERROR] " + str(e))

		return False