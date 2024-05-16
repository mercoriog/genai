import gradio as gr

def getImageOutput():
    image_output = gr.Image(
        label = "Generated image:",
        height = 512,
        width = 512
    )
    return image_output

def getAdvImageOutput():
    adv_image_output = gr.Image(
        label = "Generated image:",
        height = 512
    )
    return adv_image_output