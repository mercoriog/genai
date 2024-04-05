import gradio as gr
import examples as ex
import garments as gars
import comfyui_api as comfy

# gestione feedback
def getFeedback(positive_prompt, negative_prompt):
    callback.flag([positive_prompt, negative_prompt])

# combine user's choices to build the correct one and only positive prompt
def buildPositivePrompt(gender_input, hair_color_input, eyes_color_input, positive_prompt, items_gallery):
    item_description = gar.getGarmentDescription(items_gallery)

    fixed_positive_prompt = 
        f"full body photo of {hair_color_input} {gender_input} model wearing {item_description}, " +
        f"{eyes_color_input}:1.2, realistic face, " +
        f"{positive_prompt}"
    
    return fixed_positive_prompt

# GUI builder method:
def buildGUI():
    with gr.Blocks(title = "Txt-to-img generator", fill_height = True) as demo:
        presentation.render()
        with gr.Row():   
            with gr.Column():
                hair_color_input.render()
                eyes_color_input.render()
                positive_prompt.render()
                negative_prompt.render()
               
                with gr.Row():
                    clear_button.render()
                    generate_button.render()

            items_gallery.render()

        examples_gallery.render()
        image_output.render()
        flag_button.render()

        # combine user's choices to build positive prompt:
        fixed_positive_prompt = buildPositivePrompt(
            gender_input, 
            hair_color_input, 
            eyes_color_input, 
            positive_prompt, 
            items_gallery
        )
        
        return demo

#GUI elements:
presentation = gr.Markdown('''
    # StableDiffusion - LoRA image generator.
    Compile both positive and negative prompt to generate an image with selected garment.
''')

gender_input = gr.Radio(
    choices = ["Male", "Female"],
    value = "Male",
    label = "Select gender:",
    interactive = True
)

hair_color_input = gr.Radio(
    choices = ["Black", "Blonde", "Ginger"], 
    value = "Blonde",
    label = "Select hair color:",
    interactive = True
)

eyes_color_input = gr.Radio(
    choices = ["Black", "Green", "Blue"],
    value = "Blue",
    label = "Select eyes color:",
    interactive = True
)

positive_prompt = gr.Textbox(
    lines = 3,
    label = "Positive prompt",
    placeholder = "Type the content to generate. Use keyword.",
    show_copy_button = True
)

negative_prompt = gr.Textbox(
    lines = 3,
    label = "Negative prompt",
    placeholder = "Type what should not generate.",
    show_copy_button = True
)

items_gallery = gr.Gallery(
    value = gars.getGarmentsList(),
    format = "png",
    label = "Select garment:", 
    show_label = True, 
    min_width = 320,
    height = 480, 
    allow_preview = True, 
    preview = True, 
    selected_index = 0
)

clear_button = gr.ClearButton(
    components = [positive_prompt, negative_prompt],
    value = "Clear prompts",
    variant = "secondary"
)


image_output = gr.Image(
    label = "Generated image:",
    height = 480,
    width = 320
)

generate_button = gr.Button(
    value = "Generate image",
    variant = "primary"
)

generate_button.click(
    fn = comfy.generateImage, 
    inputs = [fixed_positive_prompt, negative_prompt],
    outputs = [image_output],
    scroll_to_output = True,
    show_progress = "minimal"
)

# examples:
examples_list = ex.getExamples()
examples_gallery = gr.Examples(
    examples = examples_list,
    inputs = [
        gender_input, 
        hair_color_input, 
        eyes_color_input, 
        positive_prompt, 
        negative_prompt, 
        image_output
    ],
    label = "Examples:"
)


# flag setup:
# flagger object to save user's feedkback
callback = gr.CSVLogger()

# flagging callback configuration
callback.setup(
    [positive_prompt, negative_prompt], 
    "flagged_prompts"
)

flag_button = gr.Button(
    value = "Report incorrect image", 
    variant = "stop"
)

flag_button.click(
    fn = getFeedback,
    inputs = [positive_prompt, negative_prompt],
    preprocess = False
)