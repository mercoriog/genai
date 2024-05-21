import gradio as gr

def getPresentation():
    presentation = gr.Markdown('''
        # StableDiffusion - LoRA image generator.
        Compile both positive and negative prompt to tell AI Model what you want to generate. \n
        Selecting an item from gallery will automatically insert the correct token in positive prompt. \n
        Click 'Generate image' button to perform the generation request.
    ''')
    return presentation

def getSettingsPresentation():
    presentation = gr.Markdown('''
        # StableDiffusion - LoRA image generator.
        Set workflow api settings.
    ''')
    return presentation