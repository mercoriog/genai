import gradio as gr
from component import button 
from component import example  
from component import highlightedText
from component import image  
from component import markdown 
from component import radio 
from component import gallery 
from component import textbox
from examples import controller as ctrlEx
from gallery import controller as ctrlGal
from gui import script

# GUI builder method:
def buildGUI():
    with gr.Blocks(title = "Txt-to-img generator") as demo:
        # [NEW] TAB SECTION:
        with gr.Tab("Standard"):
            # TEXTUAL DESCRIPTION:
            presentation = markdown.getPresentation()

            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                # [NEW] VERTICAL LAYOUT:
                with gr.Column():
                    gender_input = radio.getGenderInput()
                    hair_color_input = radio.getHairColorInput()
                    eyes_color_input = radio.getEyesColorInput()
                # [END] VERTICAL LAYOUT.
                
                # [NEW] VERTICAL LAYOUT:
                with gr.Column():
                    positive_prompt = textbox.getPositivePrompt()
                    negative_prompt = textbox.getNegativePrompt()
                # [END] VERTICAL LAYOUT.
            # [END] HORIZONTAL LAYOUT.

            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                # Get avaible images in gallery.
                gallery_images = ctrlGal.getGalleryImages()

                # Create gallery with retrived avaible images.
                items_gallery = gallery.getItemsGallery(gallery_images)
                image_output = image.getImageOutput()
            # [END] HORIZONTAL LAYOT.

            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                clear_button = button.getStandardClearButton(positive_prompt, negative_prompt, image_output)
                generate_button = button.getGenerateButton()
            # [END] HORIZONTAL LAYOUT.

            # Retrive avaible examples.
            avaible_examples = ctrlEx.getExamples()

            # Build exampleBox.
            exampleBox = (image_output, gender_input, hair_color_input, eyes_color_input, positive_prompt, negative_prompt,avaible_examples)

            # Build examples gallery from avaible examples.
            examples_gallery = example.getExamplesGallery(examplebox)

            # Fake component to store selected item in gallery.
            selected_item_gallery = textbox.getSelItemGallery()
            
            def getSelectItemGallery(evt: gr.SelectData):
                return evt.index

            # Select item in gallery event:
            items_gallery.select(
                fn = getSelectItemGallery, 
                inputs = None, 
                outputs = selected_item_gallery
            )

            # generate image event:
            generate_button.click(
                fn = script.generateImage, 
                inputs = [
                    gender_input, 
                    hair_color_input, 
                    eyes_color_input, 
                    positive_prompt, 
                    selected_item_gallery, 
                    negative_prompt
                ],
                outputs = [image_output],
                scroll_to_output = True,
                show_progress = "minimal"
            )

        # [END] TAB SECTION.

        # [NEW] TAB SECTION:
        with gr.Tab("Advanced"):
            adv_presentation = markdown.getAdvPresentation()
            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                # [NEW] VERTICAL LAYOUT:
                with gr.Column():
                    adv_positive_prompt = textbox.getPositivePrompt()
                    adv_negative_prompt = textbox.getNegativePrompt()

                    ordered_garments = ctrlGal.getOrderedGarments()
                    avaible_garments_list = highlightedText.getAvaibleGramentsList(ordered_garments)
                # [END] VERTICAL LAYOUT.
                
                # [NEW] VERTICAL LAYOUT:
                with gr.Column():
                    adv_image_output = image.getAdvImageOutput()
                # [END] VERTICAL LAYOUT.
            # [END] HORIZONTAL LAYOUT.
            
            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():
                adv_clear_button = button.getAdvancedClearButton(adv_positive_prompt, adv_negative_prompt)
                adv_generate_button = button.getGenerateButton()
            # [END] HORIZONTAL LAYOUT.

            # generate image event:
            adv_generate_button.click(
                fn = script.generateImage,
                inputs = [adv_positive_prompt, adv_negative_prompt],
                outputs = [adv_image_output],
                scroll_to_output = True,
                show_progress = "minimal"
            )

        # [END] TAB SECTION.
        return demo