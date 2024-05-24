from comfyui import controller as ctrlComfy
from gallery import controller as ctrlGal
import gradio as gr
import json

# combine user's choices to build the correct one and only positive prompt
def buildPositivePrompt(positive_prompt, gallery_item):
    # Get gallery items names.
    gallery_names = ctrlGal.getGalleryNames()
    
    # Build positive prompt with user inputs.
    fixed_positive_prompt = f"{gallery_names[int(gallery_item)]}:1.5, {positive_prompt}"
    
    # Return correct positive prompt.
    return fixed_positive_prompt

def generate(positive_prompt, gallery_item, negative_prompt):
    if gallery_item:
        positive_prompt = buildPositivePrompt(positive_prompt, gallery_item)

    generated_image = ctrlComfy.generateRemoteImage(positive_prompt, negative_prompt)

    return generated_image

def getProvidedWorkflow():
    return ctrlComfy.getProvidedWorkflow()

def getJSONCurrentWorkflow():
    json_file = ctrlComfy.getCurrentWorkflow()

    with open(json_file, "r") as file:
        data = file.read()

    json_string = json.loads(data)

    return json_string

def getCurrentURL():
    return ctrlComfy.getCurrentURL()


def updateSettings(comfyURL_textbox, workflow_file):
    if workflow_file:
        # Save user workflow.
        work_saved = ctrlComfy.saveWorkflow(workflow_file)

        if not work_saved:
            gr.Error("Workflow not updated.")
        else:
            gr.Info("Settings updated.")

    if comfyURL_textbox:
        # Save user URL.
        url_saved = ctrlComfy.saveURL(comfyURL_textbox)

        if not url_saved:
            gr.Error("URL not updated.")
        else:
            gr.Info("Settings updated.")

    current_URL = getCurrentURL()
    current_workflow = getJSONCurrentWorkflow()

    return current_URL, current_workflow

    
