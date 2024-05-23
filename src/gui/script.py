from comfyui import controller as ctrlComfy
from gallery import controller as ctrlGal
import gradio as gr

# combine user's choices to build the correct one and only positive prompt
def buildPositivePrompt(positive_prompt, gallery_item):
    # Get gallery items names.
    gallery_names = ctrlGal.getGalleryNames()
    
    # Build positive prompt with user inputs.
    fixed_positive_prompt = f"{gallery_names[int(gallery_item)]}:1.5, {positive_prompt}"
    
    # Return correct positive prompt.
    return fixed_positive_prompt

def generate(positive_prompt, gallery_item, negative_prompt):
	positive_prompt = buildPositivePrompt(positive_prompt, gallery_item)
	
	generated_image = ctrlComfy.generateImage(positive_prompt, negative_prompt)

	return generated_image

def updateSettings(comfyURL_textbox, workflow_file):
    gr.Info("Settings updated.")
