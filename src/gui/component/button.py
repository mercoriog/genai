import gradio as gr

def getStandardClearButton(positive_prompt, negative_prompt, image_output):
    clear_button = gr.ClearButton(
        components = [positive_prompt, negative_prompt, image_output],
        value = "Clear",
        variant = "secondary"
    )
    return clear_button

def getAdvancedClearButton(positive_prompt, negative_prompt):
    clear_button = gr.ClearButton(
        components = [positive_prompt, negative_prompt],
        value = "Clear prompts",
        variant = "secondary"
    )
    return clear_button

def getGenerateButton():
    generate_button = gr.Button(
        value = "Generate image",
        variant = "primary"
    )
    return generate_button