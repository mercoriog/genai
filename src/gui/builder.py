import gradio as gr
from examples import controller as ex
from gallery import controller as gal
from comfyui import controller as comfy
from gui import components as comp

def getOrderedGarments():
    garments_list = gal.getGalleryNames()
    ordered_garments = []
    count = 0

    for item in garments_list:
        count += 1
        ordered_garments.append((item, count))
    
    return ordered_garments

# combine user's choices to build the correct one and only positive prompt
def buildPositivePrompt(gender, hair_color, eyes_color, positive_prompt, selected_item):
    # Get gallery items names.
    gallery_names = gal.getGalleryNames()

    # Build positive prompt with user inputs.
    fixed_positive_prompt = f"full body photo of {hair_color_input} \
        {gender_input} model wearing {gallery_names[selected_item]}:1.2, \
        {eyes_color_input}:1.2, \
        realistic face, \
        {positive_prompt}"
    
    # Return correct positive prompt.
    return fixed_positive_prompt

# GUI builder method:
def buildGUI():
    with gr.Blocks(title = "Txt-to-img generator") as demo:
        # [NEW] TAB SECTION:
        with gr.Tab("Standard"):
            # TEXTUAL DESCRIPTION:
            presentation = comp.getPresentation()

            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                # [NEW] VERTICAL LAYOUT:
                with gr.Column():
                    gender_input = comp.getGenderInput()
                    hair_color_input = comp.getHairColorInput()
                    eyes_color_input = comp.getEyesColorInput()
                # [END] VERTICAL LAYOUT.
                
                # [NEW] VERTICAL LAYOUT:
                with gr.Column():
                    positive_prompt = comp.getPositivePrompt()
                    negative_prompt = comp.getNegativePrompt()
                # [END] VERTICAL LAYOUT.
            # [END] HORIZONTAL LAYOUT.

            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                gallery_images = gal.getGalleryImages()
                items_gallery = comp.getItemsGallery(gallery_images)
                image_output = comp.getImageOutput()
            # [END] HORIZONTAL LAYOT.

            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                clear_button = comp.getStandardClearButton(positive_prompt, negative_prompt, image_output)
                generate_button = comp.getGenerateButton()
            # [END] HORIZONTAL LAYOUT.

            avaible_examples = ex.getExamples()

            examples_gallery = comp.getExamplesGallery(image_output, gender_input, hair_color_input, eyes_color_input, positive_prompt, negative_prompt,avaible_examples)

            # combine user's choices to build positive prompt:
            fixed_positive_prompt = buildPositivePrompt(gender_input, hair_color_input, eyes_color_input, positive_prompt, items_gallery)
            
            # fake component to store fixed positive prompt
            fixed_component = comp.getFixedComponent(fixed_positive_prompt)

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
            adv_presentation = comp.getAdvPresentation()
            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                # [NEW] VERTICAL LAYOUT:
                with gr.Column():
                    adv_positive_prompt = comp.getPositivePrompt()
                    adv_negative_prompt = comp.getNegativePrompt()

                    ordered_garments = getOrderedGarments()
                    avaible_garments_list = comp.getAvaibleGramentsList(ordered_garments)
                # [END] VERTICAL LAYOUT.
                
                # [NEW] VERTICAL LAYOUT:
                with gr.Column():
                    adv_image_output = comp.getAdvImageOutput()
                # [END] VERTICAL LAYOUT.
            # [END] HORIZONTAL LAYOUT.
            
            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                adv_clear_button = comp.getAdvancedClearButton(adv_positive_prompt, adv_negative_prompt)
                adv_generate_button = comp.getGenerateButton()
            # [END] HORIZONTAL LAYOUT.

            # generate image event:
            adv_generate_button.click(
                fn = comfy.generateImage,
                inputs = [adv_positive_prompt, adv_negative_prompt],
                outputs = [adv_image_output],
                scroll_to_output = True,
                show_progress = "minimal"
            )

        # [END] TAB SECTION.
        return demo