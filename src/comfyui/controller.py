from comfyui import output as comfyOUT
from comfyui import comfyURL
from comfyui import workflow as comfyWORK
from gallery import controller as gal
import json
import os
import requests
import time

def startQueue(prompt_workflow, URL):
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

    # Get ComfyUI API URL.
    URL = comfyURL.getURL()

    # Get ComfyUI output folder.
    output_folder = comfyOUT.getOutputFolderPath()

    # Get latest image in folder before generating new one 
    # and storing it in the same folder.
    # This latest image will be the [OLD]_latest_image.
    previous_image = comfyOUT.getLatestImage(output_folder)

    # Get workflow file.
    workflow_file = comfyWORK.getWorkflowFilePath()

    # Update workflow file with positive and negative prompt.
    prompt = comfyWORK.updateWorkflow(positive_prompt, negative_prompt, workflow_file)

    # Call the API to generate the image.
    startQueue(prompt, URL)

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