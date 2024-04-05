import json
import os
import time
import random
import numpy as np
import requests

# ComfyUI's API URL
URL = "http://127.0.0.1:8188/prompt"

INPUT_DIR = "replace with comfyui input dir path"

# output folder's path of ComfyUI
OUTPUT_DIR = "replace with comfyui ouput directory path"

# retrive last image in folder
def getLatestImage(folder):
    files = os.listdir(folder)
    # filter image format file
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)))
    latest_image = os.path.join(folder, image_files[-1]) if image_files else None
    return latest_image

# method that interacts with ComfyUI's API
def startQueue(prompt_workflow):
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    requests.post(URL, data=data)

# main method to generate images
def generateImage(positive_prompt, negative_prompt):
    # open the workflow.json file to set both prompts and the seed number:
    with open("genai\\source\\workflow_api.json", "r") as file_json:
        # load the json file 
        prompt = json.load(file_json)
        # set positive and negative prompts
        prompt["6"]["inputs"]["text"] = f"{positive_prompt}"
        prompt["7"]["inputs"]["text"] = f"{negative_prompt}"

        # set a random seed that maps one image biunivocally
        prompt["3"]["inputs"]["seed"] = random.randint(1, 1500000)
    
    # get latest image in folder before generating one and store it in the same folder
    # this latest image will be the [OLD]_latest_image 
    previous_image = getLatestImage(OUTPUT_DIR)
    
    # call the API to generate the image
    startQueue(prompt)

    while True:
        # until i find a new image in output folder
        latest_image = getLatestImage(OUTPUT_DIR)
        
        # if the latest image isn't the same of the [OLD]_latest_image means that new generated image is stored in output folder
        if latest_image != previous_image:
            return latest_image 

        # setting a waiting timing to looking for new generated image in folder
        time.sleep(1)