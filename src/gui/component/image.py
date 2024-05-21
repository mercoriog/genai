import gradio as gr

def getImageOutput():
    image_output = gr.Image(
        label = "Generated image:",
        width = 512
    )
    return image_output