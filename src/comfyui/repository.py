from repository import comfyui as comfylib
import os 

# ComfyUI's API URL
URL = "http://127.0.0.1:8188/prompt"

# Workflow api json file name.
WORKFLOW_JSON = "workflow_api.json"

# Output folder path of ComfyUI in local machine.
OUTPUT_DIR = "replace with comfyui ouput directory path"

def getURL():
    # Return ComfyUI API URL.
    return URL

def getWorkflowFilePath():
    # Get 'comfyui' folder path.
    comfyui_folder_path = comfylib.getFolderPath()

    # Build workflow file path.
    workflow_file_path = os.path.join(comfyui_folder_path, WORKFLOW_JSON)

    # Return Workflow file path.
    return workflow_file_path

def getOutputFolderPath():
    # Return output folder path.
    return OUTPUT_DIR
