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
            with gr.Accordion(label = "Select item", open = True):
                
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
            
            with gr.Accordion("Current settings:", open = False):
                # Get URL.
                currentURL= script.getCurrentURL()

                # Display URL.
                currentURL_textbox = textbox.getCurrentURLtextbox(currentURL)

                # Get Current Workflow.
                currentWorkflow_json = script.getJSONCurrentWorkflow()

                # Display current Workflow.
                workflow_json_show = JSON.getWorkflowJSON(currentWorkflow_json)

            # Change setting presentation.
            change_setting_presentation = markdown.getChangeSettingMarkdown()

            # Textbot to insert coustom ComfyUI URL:
            comfyURL_textbox = textbox.getComfyURLTextbox()

            # File uploader for .json workflow file.
            workflow_file = file.getWorkflowFile()

            # Set update button.
            update_settings_button = button.getUpdateSettingsButton()

            # Update button event:
            update_settings_button.click(
                fn = script.updateSettings, 
                inputs = [comfyURL_textbox, workflow_file],
                outputs = [currentURL_textbox, workflow_json_show]
            )

            # Set clear button.
            clear_settings_button = button.getClearSettingsButton(comfyURL_textbox, workflow_file)

            with gr.Accordion("Provided workflow", open = False):
                # Get provided workflow filepath.
                provided_workflow_json = script.getProvidedWorkflow()
                
                # Set provided workflow file downloader.
                provided_workflow_file = file.getProvidedWorkflow(provided_workflow_json)

        # [END] TAB SECTION.
        
        return demo