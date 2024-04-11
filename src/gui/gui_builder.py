import gradio as gr
import gui.examples.examples as ex
import gui.garments as gars
import gui.comfyui.comfyui_api as comfy

def compgetPresentation():
    presentation = gr.Markdown('''
        # StableDiffusion - LoRA image generator.
        Compile both positive and negative prompt to generate an image with selected garment.
        Select model's traits using radio buttons choices.
    ''')
    return presentation

def compgetAdvPresentation():
    presentation = gr.Markdown('''
        # StableDiffusion - LoRA image generator.
        Compile both positive and negative prompt to generate an image.
    ''')
    return presentation

def compgetGenderInput():
    gender_input = gr.Radio(
        choices = ["Male", "Female"],
        value = "Male",
        label = "Select gender:",
        interactive = True
    )
    return gender_input

def compgetHairColorInput():
    hair_color_input = gr.Radio(
        choices = ["Black", "Blonde", "Ginger"], 
        value = "Blonde",
        label = "Select hair color:",
        interactive = True
    )
    return hair_color_input

def compgetEyesColorInput():
    eyes_color_input = gr.Radio(
        choices = ["Black", "Green", "Blue"],
        value = "Blue",
        label = "Select eyes color:",
        interactive = True
    )
    return eyes_color_input

def compgetPositivePrompt():
    positive_prompt = gr.Textbox(
        lines = 3,
        label = "Positive prompt",
        placeholder = "Type the content to generate. Use keyword.",
        show_copy_button = True,
        interactive = True
    )
    return positive_prompt

def compgetNegativePrompt():
    negative_prompt = gr.Textbox(
        lines = 3,
        label = "Negative prompt",
        placeholder = "Type what should not generate.",
        show_copy_button = True,
        interactive = True
    )
    return negative_prompt

def compgetImageOutput():
    image_output = gr.Image(
        label = "Generated image:",
        height = 512,
        width = 512
    )
    return image_output

def compgetAdvImageOutput():
    adv_image_output = gr.Image(
        label = "Generated image:",
        height = 512
    )
    return adv_image_output

def compgetItemsGallery():
    items_gallery = gr.Gallery(
        value = gars.getGarmentsImagesList(),
        format = "png",
        label = "Select garment:", 
        show_label = True, 
        min_width = 512,
        height = 512, 
        allow_preview = True,
        selected_index = 0
    )
    return items_gallery

def compgetStandardClearButton(positive_prompt, negative_prompt, image_output):
    clear_button = gr.ClearButton(
        components = [positive_prompt, negative_prompt, image_output],
        value = "Clear",
        variant = "secondary"
    )
    return clear_button

def compgetAdvancedClearButton(positive_prompt, negative_prompt):
    clear_button = gr.ClearButton(
        components = [positive_prompt, negative_prompt],
        value = "Clear prompts",
        variant = "secondary"
    )
    return clear_button

def compgetGenerateButton():
    generate_button = gr.Button(
        value = "Generate image",
        variant = "primary"
    )
    return generate_button

def compgetExamplesGallery(
    image_output,
    gender_input, 
    hair_color_input, 
    eyes_color_input, 
    positive_prompt, 
    negative_prompt
    ):
    
    examples_gallery = gr.Examples(
        examples = ex.getExamples(),
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

def orderGarments(garments_list):
    ordered_garments = []
    count = 0

    for item in garments_list:
        count += 1
        ordered_garments.append((item, count))
    
    return ordered_garments

def compgetAvaibleGramentsList():
    # obtain garments list and order them to match the 'value' param of gr.HighlightedText object
    ordered_garments = orderGarments(gars.getGarmentsList())
    avaible_garments_list = gr.HighlightedText(
        value = ordered_garments,
        label = "Avaible garments:",
        show_label = True,
        interactive = False
    )
    return avaible_garments_list

def compgetFixedComponent(fixed_positive_prompt):
    fixed_component = gr.Textbox(
        value = fixed_positive_prompt,
        render = False
    )
    return fixed_component

# combine user's choices to build the correct one and only positive prompt
def buildPositivePrompt(
    gender_input, 
    hair_color_input, 
    eyes_color_input, 
    positive_prompt, 
    items_gallery
    ):
    
    item_description = gars.getGarmentDescription(items_gallery)

    fixed_positive_prompt = f"full body photo of {hair_color_input} \
        {gender_input} model wearing {item_description}:1.2, \
        {eyes_color_input}:1.2, \
        realistic face, \
        {positive_prompt}"
        
    return fixed_positive_prompt

# GUI builder method:
def buildGUI():
    with gr.Blocks(title = "Txt-to-img generator") as demo:
        # [NEW] TAB SECTION:
        with gr.Tab("Standard"):
            # TEXTUAL DESCRIPTION:
            presentation = compgetPresentation()

            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                # [NEW] VERTICAL LAYOUT:
                with gr.Column():
                    gender_input = compgetGenderInput()
                    hair_color_input = compgetHairColorInput()
                    eyes_color_input = compgetEyesColorInput()
                # [END] HORIZONTAL LAYOUT.
                
                # [NEW] VERTICAL LAYOUT:
                with gr.Column():
                    positive_prompt = compgetPositivePrompt()
                    negative_prompt = compgetNegativePrompt()
                # [END] VERTICAL LAYOUT.
            # [END] HORIZONTAL LAYOUT.

            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                items_gallery = compgetItemsGallery()
                image_output = compgetImageOutput()
            # [END] HORIZONTAL LAYOT.

            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                clear_button = compgetStandardClearButton(
                    positive_prompt, 
                    negative_prompt, 
                    image_output
                )
                generate_button = compgetGenerateButton()
            # [END] HORIZONTAL LAYOUT.

            examples_gallery = compgetExamplesGallery(
                image_output,
                gender_input, 
                hair_color_input, 
                eyes_color_input, 
                positive_prompt, 
                negative_prompt
            )

            # combine user's choices to build positive prompt:
            fixed_positive_prompt = buildPositivePrompt(
                gender_input, 
                hair_color_input, 
                eyes_color_input, 
                positive_prompt, 
                items_gallery
            )
            
            # fake component to store fixed positive prompt
            fixed_component = compgetFixedComponent(fixed_positive_prompt)

            # generate image event:
            generate_button.click(
                fn = comfy.generateImage, 
                inputs = [fixed_component, negative_prompt],
                outputs = [image_output],
                scroll_to_output = True,
                show_progress = "minimal"
            )

        # [END] TAB SECTION.

        # [NEW] TAB SECTION:
        with gr.Tab("Advanced"):
            adv_presentation = compgetAdvPresentation()
            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                # [NEW] VERTICAL LAYOUT:
                with gr.Column():
                    adv_positive_prompt = compgetPositivePrompt()
                    adv_negative_prompt = compgetNegativePrompt()
                    avaible_garments_list = compgetAvaibleGramentsList()
                # [END] VERTICAL LAYOUT.
                
                # [NEW] VERTICAL LAYOUT:
                with gr.Column():
                    adv_image_output = compgetAdvImageOutput()
                # [END] VERTICAL LAYOUT.
            # [END] HORIZONTAL LAYOUT.
            
            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                adv_clear_button = compgetAdvancedClearButton(
                    adv_positive_prompt, 
                    adv_negative_prompt
                )
                adv_generate_button = compgetGenerateButton()
            # [END] HORIZONTAL LAYOUT.

            # generate image event:
            adv_generate_button.click(
                fn = comfy.generateImage,
                inputs = [adv_positive_prompt, adv_negative_prompt],
                outputs = [adv_image_output],
                scroll_to_output = True,
                show_progress = "minimal"
            )

        # [END] TAB SECTION:
        return demo