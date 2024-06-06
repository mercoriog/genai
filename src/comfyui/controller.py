from comfyui import comfyURL
from comfyui import workflow as comfyWORK
from comfyui import script
from comfyui import prompt
from gallery import controller as gal

def generateWebSocketImage(positive_prompt, negative_prompt):
    # This function generate a new image using positive and negative prompt.
    # It process a request to comfyui API using both prompts
    # and use webSocket to retrive image.
    
    # Get ComfyUI API URL.
    URL = comfyURL.getURL()

    # Get workflow file.
    workflow_file = comfyWORK.getCurrentWorkflow()

    # Update workflow file with positive and negative prompt.
    prompt_workflow = comfyWORK.updateWorkflow(positive_prompt, negative_prompt, workflow_file)

    # Perform WebSocket generation with:
    # <URL> of the target machine, 
    # <prompt> for the body of generation.
    image = script.webSocketGeneration(prompt_workflow, URL)

    # Return generated image (can be None if an error occurs).
    return image
    
def saveWorkflow(workflow_file):
    # Save user workflow.
    return comfyWORK.saveNewWorkflow(workflow_file)

def saveURL(URL):
    # Save user workflow.
    return comfyURL.saveNewURL(URL)

def savePrompts(prompt_matrix):
    # Save prompt matrix.
    return prompt.savePrompts(prompt_matrix)

def getProvidedWorkflow():
    return comfyWORK.getWorkflowFilePath()

def getCurrentWorkflow():
    return comfyWORK.getCurrentWorkflow()

def getCurrentURL():
    return comfyURL.getURL()

def getCurrentPrompts():
    return prompt.getCurrentPrompts()