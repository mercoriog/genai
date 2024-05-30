from repository import comfyui as comfylib
from comfyui import prompt as comfyPrompt
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

def getUserWorkflowFilePath():
    # Get 'comfyui' folder path.
    comfyui_folder_path = comfylib.getFolderPath()

    # Build user_workflow file path.
    user_workflow_path = os.path.join(comfyui_folder_path, "user_" + WORKFLOW_JSON)

    # Return user workflow file path.
    return user_workflow_path

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

        # Get current prompts combination.
        prompt_matrix = comfyPrompt.getCurrentPrompts()

        for row in prompt_matrix:
            # Get positive from matrix.
            positive_index = row[0]
            
            # Set positive prompt.
            prompt[str(positive_index)]["inputs"]["text"] = f"{positive_prompt}"

            # Set negative prompt.
            negative_index = row[1]
            
            # Set negative prompt.
            prompt[str(negative_index)]["inputs"]["text"] = f"{negative_prompt}"

            seed = random.randint(1, 1500000)

            # Get seed.
            seed_index = row[2]
            
            # Set a random seed that maps one image biunivocally.
            prompt[str(seed_index)]["inputs"]["seed"] = seed

        # Close workflow file.
        file_json.close()

        # If no error occurs, return the processed prompt json file. 
        return prompt

    # An error occurs:
    except Exception as e:
        # Print the exception.
        print("[ERROR] Update workflow failed: " + str(e))

        # Return False if error occurs.
        return None
    
def saveNewWorkflow(workflow_file):
    # Set an exception handler:
    try:
        user_workflow_path = getUserWorkflowFilePath()
        
        # Save user workflow. 
        shutil.copy(workflow_file, user_workflow_path)

        # Return True if copy operation done.
        return True

     # An error occurs:
    except Exception as e:
        # Print the exception.
        print("[ERROR] " + str(e))

        # Return False if error occurs.
        return False

def getCurrentWorkflow():
    # Get user workflow file path.
    user_workflow_path = getUserWorkflowFilePath()

    # Get provide workflow file path.
    provided_workflow = getWorkflowFilePath()

    if os.path.exists(user_workflow_path):
        return user_workflow_path
    else:
        return provided_workflow





