import gradio as gr

def getPositivePrompt():
    positive_prompt = gr.Textbox(
        lines = 4,
        label = "Positive prompt",
        placeholder = "Type the content to generate. Use keyword.",
        show_copy_button = True,
        interactive = True
    )
    return positive_prompt

def getNegativePrompt():
    negative_prompt = gr.Textbox(
        lines = 4,
        label = "Negative prompt",
        placeholder = "Type what should not generate.",
        show_copy_button = True,
        interactive = True
    )
    return negative_prompt

def getFixedComponent(fixed_positive_prompt):
    fixed_component = gr.Textbox(
        value = fixed_positive_prompt,
        render = False
    )
    return fixed_component

def getSelItemGallery():
    selected_index_textbox = gr.Textbox(
        value = "0", 
        visible = False
    )
    return selected_index_textbox

def getComfyURLTextbox():
    comfyURL_textbox = gr.Textbox(
        lines = 1,
        label = "ComfyUI URL",
        placeholder = "Type running ComfyUI URL. Leave blank to use default URL: 'http://127.0.0.1:8188/prompt'",
        show_copy_button = True,
        interactive = True
    )
    return comfyURL_textbox

def getComfyOutputTextbox():
    comfyOutput = gr.Textbox(
        lines = 1,
        label = "ComfyUI local folder path",
        placeholder = "Tyoe running ComfyUI folder path.",
        show_copy_button = True,
        interactive = True
    )
