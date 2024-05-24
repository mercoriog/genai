from repository import comfyui as comfylib
import os
import random
import json
import shutil

# Workflow api json file name.
WORKFLOW_JSON = "workflow_api.json"

def getWorkflowFilePath():
    # Get 'comfyui' folder path.
    comfyui_folder_path = comfylib.getFolderPath()

    # Build workflow file path.
    workflow_file_path = os.path.join(comfyui_folder_path, WORKFLOW_JSON)

    # Return Workflow file path.
    return workflow_file_path

def updateWorkflow(positive_prompt, negative_prompt, workflow_file):
    # This function updates the comfyui workflow json file using provided
    # positive and negative prompt.
    # This function also set a random seed for image generation.

    # Set an exception handler:
    try:
        # Open the workflow json file.
        file_json = open(workflow_file, "r")

        # Load json file.
        prompt = json.load(file_json)

        # Set positive prompt.
        prompt["6"]["inputs"]["text"] = f"{positive_prompt}"

        # Set negative prompt.
        prompt["7"]["inputs"]["text"] = f"{negative_prompt}"

        # Set a random seed that maps one image biunivocally.
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

def saveWorkflow(workflow_file):
    # Get 'comfyui' folder path.
    comfyui_folder_path = comfylib.getFolderPath()

    # Get 'comfyui'
    # 
    shutil.copy(workflow_file)
