import gradio as gr

def getExamplesGallery(examplebox):
    # <examplebox> prevede è una 7-pla contenente:
    # 0 - image_output
    # 1 - gender_input
    # 2 - hair_color_input
    # 3 - eyes_color_input 
    # 4 - positive_prompt 
    # 5 - negative_prompt
    # 6 - examples

    examples_gallery = gr.Examples(
        examples = examplebox[6],
        inputs = [
            examplebox[0],
            examplebox[1], 
            examplebox[2], 
            examplebox[3], 
            examplebox[4], 
            examplebox[5]
        ],
        label = "Examples:"
    )
    return examples_gallery