import gradio as gr

def getExamplesGallery(image_output, positive_prompt, negative_prompt, avaible_examples):

    examples_gallery = gr.Examples(
        examples = avaible_examples,
        inputs = [
            image_output,
            positive_prompt,
            negative_prompt
        ],
        examples_per_page = 1,
        label = "Examples:"
    )
    return examples_gallery