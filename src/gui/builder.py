import gradio as gr
from .component import *
from examples import controller as ctrlEx
from gallery import controller as ctrlGal
from gui import script

# GUI builder method:
def buildGUI():
    
    # Define gradio GUI body:
    with gr.Blocks(title = "Txt-to-img generator") as demo:
        
        # [NEW] TAB SECTION:
        with gr.Tab("Generator"):
            
            # TEXTUAL DESCRIPTION:
            presentation = markdown.getPresentation()

            # [NEW] DYNAMIC SECTION:
            with gr.Accordion(label = "Select item", open = False):
                # Get avaible images in gallery.
                gallery_images = ctrlGal.getOrderedImages()
            
                # Create gallery with retrived avaible images.
                items_gallery = gallery.getItemsGallery(gallery_images)
            # [END] DYNAMIC SECTION:
            
            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():

                # Set positive prompt input textbox.
                positive_prompt = textbox.getPositivePrompt()

                # Set negative prompt input textbox.
                negative_prompt = textbox.getNegativePrompt()
            
            # [END] HORIZONTAL LAYOUT.

            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():

                # Set output image box.
                image_output = image.getImageOutput()

                # Retrive avaible examples.
                avaible_examples = ctrlEx.getExamples()

                # Build examples gallery from avaible examples.
                examples_gallery = example.getExamplesGallery(image_output, positive_prompt, negative_prompt,avaible_examples)
                
            # [END] HORIZONTAL LAYOT.

            # [NEW] HORIZONTAL LAYOUT:
            with gr.Row():

                # Set button to perform request.
                generate_button = button.getGenerateButton()

                # Set clear button to clear components data.
                clear_button = button.getStandardClearButton(positive_prompt, negative_prompt, image_output)
            
            # [END] HORIZONTAL LAYOUT.

            # Fake component to store selected item in gallery.
            selected_item_gallery = textbox.getSelItemGallery()
            
            # Inner function to handle selected item event:
            def getSelectItemGallery(evt: gr.SelectData):
                # Return gallery item index.
                return evt.index

            # Select item in gallery event:
            items_gallery.select(
                fn = getSelectItemGallery, 
                inputs = None, 
                outputs = selected_item_gallery
            )

            # Generate image event:
            generate_button.click(
                fn = script.generate, 
                inputs = [
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
        with gr.Tab("Settings"):
            # Settings Tab description.
            settings_presentation = markdown.getSettingsPresentation()

            # Textbot to insert coustom ComfyUI URL:
            comfyURL_textbox = textbox.getComfyURLTextbox()

            # File uploader for .json workflow file.
            workflow_file = file.getWorkflowFile()

            # Textbox to insert local ComfyUI output folder.
            comfyOutput_textbox = textbox.getComfyOutputTextbox()

            # Set update button.
            update_settings_button = button.getUpdateSettingsButton()

            # Update button event:
            update_settings_button.click(
                fn = script.updateSettings, 
                inputs = [comfyURL_textbox, comfyOutput_textbox, workflow_file],
                outputs = None
            )

            # Set clear button.
            clear_settings_button = button.getClearSettingsButton(comfyURL_textbox, comfyOutput_textbox, workflow_file)

        # [END] TAB SECTION.
        return demo