import json
import os
import time
import random
import gradio as gr
import numpy as np
import requests
import examples as ex
from PIL import Image

URL = "http://127.0.0.1:8188/prompt"
INPUT_DIR = "replace with comfyui input dir path"
OUTPUT_DIR = "replace with comfyui ouput directory path"

#immagini hostate su https://postimg.cc/
garment_images = [
    Image.open("genai\\media\\gallery_images\\arman1jacket.png"),
    Image.open("genai\\media\\gallery_images\\arman1jacket2.png"), 
    Image.open("genai\\media\\gallery_images\\arman1jacket3.png"), 
    Image.open("genai\\media\\gallery_images\\arman1jacket4.png")
    ]





# recupero ultima immagine
def getLatestImage(folder):
    files = os.listdir(folder)
    # filtro le immagini 
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)))
    latest_image = os.path.join(folder, image_files[-1]) if image_files else None
    return latest_image

# avvio la generazione
def startQueue(prompt_workflow):
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    requests.post(URL, data=data)



def buildPositivePrompt(gender_input, hair_color_input, eyes_color_input, positive_prompt, items_gallery):
    item_description = getGarmentDescription(items_gallery)
    fixed_prompt = f"full body photo of {hair_color_input} {gender_input} model wearing {item_description}, {eyes_color_input}:1.2, realistic face, {positive_prompt}"
    return fixed_prompt

# funzione principale
def generateImage(gender_input, hair_color_input, eyes_color_input, positive_prompt, negative_prompt, items_gallery):
    # compilo il prompt positivo
    positive_prompt = buildPositivePrompt(gender_input, hair_color_input, eyes_color_input, positive_prompt, items_gallery)

    # apro il workflow
    with open("workflow_api.json", "r") as file_json:
        prompt = json.load(file_json)
        # compilo il prompt positivo e il prompt negativo
        prompt["6"]["inputs"]["text"] = f"{positive_prompt}"
        prompt["7"]["inputs"]["text"] = f"{negative_prompt}"

    # genero un nuovo seed a cui corrisponde biunivocamente l'immagine da generare
    prompt["3"]["inputs"]["seed"] = random.randint(1, 1500000)
    
    # ottengo l'ultima immagine
    previous_image = getLatestImage(OUTPUT_DIR)
    
    # chiamata per generare
    startQueue(prompt)

    while True:
        # finche non ho una nuova immagine nella cartella
        latest_image = getLatestImage(OUTPUT_DIR)
        if latest_image != previous_image:
            return latest_image
        # attendo un secondo a ciclo per ottimizzare la computazione
        time.sleep(1)

    # mi assicuro che il bottone del feedback sia disponibile    
    flag_button = True


# gestione feedback
def getFeedback(positive_prompt, negative_prompt):
    callback.flag([positive_prompt, negative_prompt])
    # disattivo il bottone
    flag_button.interactive = False

def getGarmentDescription(item_index):
    if item_description == 0:
        item_description="dark gray jacket, arman1jacket:1.2"
    else: item_description = ""
    return item_description


# codice per l'UI:
image_output = gr.Image(label="Generated image:", height=480, width=320)

# definisco il flagger per salvare i feedback sull'output
callback = gr.CSVLogger()

def buildGUI():
	# istanzio GUI
	with gr.Blocks(title="Txt-to-img generator", fill_height=True) as demo:
	    presentation = gr.Markdown('''
	        # StableDiffusion - LoRA image generator.
	        Compile both positive and negative prompt to generate an image with selected garment.
	        ''')

	    with gr.Row():   
	        with gr.Column():
	            gender_input = gr.Radio(choices=["Male", "Female"], value="Male", label="Select gender:", interactive=True)
	            hair_color_input = gr.Radio(choices=["Black", "Blonde", "Ginger"], value="Blonde", label="Select hair color:", interactive=True)
	            eyes_color_input = gr.Radio(choices=["Black", "Green", "Blue"], value="Blue", label="Select eyes color:", interactive=True)
	            positive_prompt = gr.Textbox(lines=3, label="Positive prompt", placeholder="Type the content to generate. Use keyword.", show_copy_button=True)
	            negative_prompt = gr.Textbox(lines=3, label="Negative prompt", placeholder="Type what should not generate.", show_copy_button=True)
	            with gr.Row():
	                clear_button = gr.ClearButton(components=[positive_prompt, negative_prompt], value="Clear prompts", variant="secondary")
	                generate_button = gr.Button(value="Generate image", variant="primary")
	        items_gallery = gr.Gallery(value=garment_images, format="png", label="Select garment:", show_label=True, min_width=320, height=480, allow_preview=True, preview=True, selected_index=0)

	    
	    # gestione esempi
	    examples_gallery = gr.Examples(
	    	examples=ex.getExamples(),
	        inputs=[gender_input, hair_color_input, eyes_color_input, positive_prompt, negative_prompt, image_output],
	        label="Examples:")

	    image_output.render()
	    flag_button = gr.Button(value="Report incorrect image", variant="stop")
	        
	    generate_button.click(
	        fn=generateImage, 
	        inputs=[gender_input, hair_color_input, eyes_color_input, positive_prompt, negative_prompt, items_gallery],
	        outputs=[image_output],
	        scroll_to_output=True,
	        show_progress="minimal")

	    # configuro il flagging callback
	    callback.setup([positive_prompt, negative_prompt], "flagged_prompts")
	    flag_button.click(fn=getFeedback, inputs=[positive_prompt, negative_prompt], preprocess=False)
	    return demo