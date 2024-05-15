from comfyui import repository as repo
import json
import os
import time
import random
import numpy as np
import requests

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

def updateWorkflow(positive_prompt, negative_prompt):
	# This function updates the comfyui workflow json file using provided
	# positive and negative prompt.
	# This function also set a random seed for image generation.
	
	# Get workflow file.
	workflow_file = repo.getWorkflowFilePath()

	# Set an exception handler:
	try:
		# Open the workflow json file.
	    file_json = open(workflow_file, "r")
        
        # Load the json file. 
        prompt = json.load(file_json)
	        
        # Set positive prompt.
        prompt["6"]["inputs"]["text"] = f"{positive_prompt}"
        
        # Set negative prompt.
        prompt["7"]["inputs"]["text"] = f"{negative_prompt}"

        # Set a random seed that maps one image biunivocally
        prompt["3"]["inputs"]["seed"] = random.randint(1, 1500000)

        # Close workflow file.
        file_json.close()
    
    # An error occurs:
	except Exception as e:
		# Print the exception.
        print("[ERROR] " + str(e))
        # Return False if error occurs.
    	return None

    # If no error occurs, return the processed prompt json file. 
    return prompt

def startQueue(prompt_workflow):
	# Set an exception handler:
	try:
	    # Build request body.
	    body = {"prompt": prompt_workflow}

	    # Encode body to process request.
	    data = json.dumps(body).encode('utf-8')

	    # Process request.
	    requests.post(URL, data=data)

	# An error occurs:
	except Exception as e:
		# Print the exception.
        print("[ERROR] " + str(e))
        # Return False if error occurs.
    	return None

    # If no error occurs, return True
    return True

def generateImage(positive_prompt, negative_prompt):
	# This function generate a new image using positive and negative prompt.
	# It process a request to comfyui API using both prompts
	# and check for new generated image stored in output folder.

	# Get output folder.
	output_folder = repo.getOutputFolderPath()

    # Get latest image in folder before generating new one 
    # and storing it in the same folder.
    # This latest image will be the [OLD]_latest_image. 
    previous_image = getLatestImage(output_folder)
    
	# Update workflow file with positive and negative prompt:
	prompt = updateWorkflow(positive_prompt, negative_prompt)
    
    # Call the API to generate the image.
    startQueue(prompt)

    # Process until the new generated image is stored in output folder.
    while True:
        # Check for latest image.
        latest_image = getLatestImage(output_folder)
        
        # Check if current latest image correspond to [OLD]_latest_image: 
        if latest_image != previous_image:
        	# If False, <latest_image> is the new generated image.
            return latest_image 

        # Setting a waiting time to looking for new generated image
        time.sleep(1)

    # By default return the [OLD]_latest_image.
    return previous_image