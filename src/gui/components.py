import gradio as gr

def getItemsGallery(gallery_images):
    items_gallery = gr.Gallery(
        value = gallery_images,
        format = "png",
        label = "Select garment:", 
        show_label = True, 
        min_width = 512,
        height = 512, 
        allow_preview = True,
        selected_index = 0
    )
    return items_gallery

def getExamplesGallery(image_output, gender_input, hair_color_input, eyes_color_input, positive_prompt, negative_prompt, examples):
    examples_gallery = gr.Examples(
        examples = examples,
        inputs = [
            image_output,
            gender_input, 
            hair_color_input, 
            eyes_color_input, 
            positive_prompt, 
            negative_prompt
        ],
        label = "Examples:"
    )
    return examples_gallery

def getAvaibleGramentsList(ordered_garments):
    avaible_garments_list = gr.HighlightedText(
        value = ordered_garments,
        label = "Avaible garments:",
        show_label = True,
        interactive = False
    )
    return avaible_garments_list

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

def getGenderInput():
    gender_input = gr.Radio(
        choices = ["Male", "Female"],
        value = "Male",
        label = "Select gender:",
        interactive = True
    )
    return gender_input

def getHairColorInput():
    hair_color_input = gr.Radio(
        choices = ["Black", "Blonde", "Ginger"], 
        value = "Blonde",
        label = "Select hair color:",
        interactive = True
    )
    return hair_color_input

def getEyesColorInput():
    eyes_color_input = gr.Radio(
        choices = ["Black", "Green", "Blue"],
        value = "Blue",
        label = "Select eyes color:",
        interactive = True
    )
    return eyes_color_input

def getPositivePrompt():
    positive_prompt = gr.Textbox(
        lines = 3,
        label = "Positive prompt",
        placeholder = "Type the content to generate. Use keyword.",
        show_copy_button = True,
        interactive = True
    )
    return positive_prompt

def getNegativePrompt():
    negative_prompt = gr.Textbox(
        lines = 3,
        label = "Negative prompt",
        placeholder = "Type what should not generate.",
        show_copy_button = True,
        interactive = True
    )
    return negative_prompt

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

def getFixedComponent(fixed_positive_prompt):
    fixed_component = gr.Textbox(
        value = fixed_positive_prompt,
        render = False
    )
    return fixed_component

def getSelItemGallery():
    selected_index_textbox = gr.Textbox(value="0", visible = False)
    return selected_index_textbox
