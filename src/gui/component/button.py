import gradio as gr

def getStandardClearButton(positive_prompt, negative_prompt, image_output):
    clear_button = gr.ClearButton(
        components = [positive_prompt, negative_prompt, image_output],
        value = "Clear",
        variant = "secondary"
    )
    return clear_button

def getGenerateButton():
    generate_button = gr.Button(
        value = "Generate image",
        variant = "primary"
    )
    return generate_button

def getUpdateSettingsButton():
    update_button = gr.Button(
        value = "Update settings",
        variant = "primary"
    )
    return update_button

def getClearSettingsButton(comfyURL_textbox, comfyURL_textbox, workflow_file):
    clear_button = gr.ClearButton(
        components = [comfyURL_textbox, comfyURL_textbox, workflow_file],
        value = "Clear",
        variant = "secondary"
    )
    return clear_button