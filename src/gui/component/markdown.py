import gradio as gr

def getPresentation():
    presentation = gr.Markdown('''
        # StableDiffusion - LoRA image generator.
        Compile both positive and negative prompt to generate an image with selected garment.
        Select model's traits using radio buttons choices.
    ''')
    return presentation

def getAdvPresentation():
    presentation = gr.Markdown('''
        # StableDiffusion - LoRA image generator.
        Compile both positive and negative prompt to generate an image.
    ''')
    return presentation