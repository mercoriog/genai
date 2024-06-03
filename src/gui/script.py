from comfyui import controller as ctrlComfy
from gallery import controller as ctrlGal
from PIL import Image
import io
import gradio as gr
import json

# combine user's choices to build the correct one and only positive prompt
def buildPositivePrompt(positive_prompt, gallery_item):
    # Get gallery items names.
    gallery_names = ctrlGal.getGalleryNames()
    
    # Build positive prompt with user inputs.
    fixed_positive_prompt = f"{gallery_names[int(gallery_item)]}:1.2, {positive_prompt}"
    
    # Return correct positive prompt.
    return fixed_positive_prompt

def generate(positive_prompt, gallery_item, negative_prompt):
    if gallery_item:
        positive_prompt = buildPositivePrompt(positive_prompt, gallery_item)

    generated_images_dict = ctrlComfy.generateWebSocketImage(positive_prompt, negative_prompt)

    generated_images_list = []

    # Itera attraverso i nodi nel dizionario
    for node_id in generated_images_dict:
        # Itera attraverso ogni immagine associata al node_id
        for image_data in generated_images_dict[node_id]:
            # Crea un oggetto Image a partire dai dati binari
            image = Image.open(io.BytesIO(image_data))
            
            generated_images_list.append(image)

    return generated_images_list[0]

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

def getCurrentPrompts():
    return ctrlComfy.getCurrentPrompts()


def updateSettings(comfyURL_textbox, workflow_file, prompt_matrix):
    if workflow_file:
        # Save user workflow.
        work_saved = ctrlComfy.saveWorkflow(workflow_file)

        if not work_saved:
            gr.Error("Workflow not updated.")
        else:
            gr.Info("Workflow updated.")

    if comfyURL_textbox:
        # Save user URL.
        url_saved = ctrlComfy.saveURL(comfyURL_textbox)

        if not url_saved:
            gr.Error("URL not updated.")
        else:
            gr.Info("URL updated.")

    if prompt_matrix:
        # Save info.
        prompts_saved = ctrlComfy.savePrompts(prompt_matrix)

        if not prompts_saved:
            gr.Error("Prompt info not updated.")
        else:
            gr.Info("Prompt info updated.")

    current_URL = getCurrentURL()
    current_workflow = getJSONCurrentWorkflow()
    current_prompts = getCurrentPrompts()

    return current_URL, current_workflow, current_prompts

    
