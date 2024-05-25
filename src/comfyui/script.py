from comfyui import output as comfyOUT
from comfyui import websocket as comfyWS
import websocket #NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import json
import requests
import uuid

def startRemoteQueue(prompt_workflow, URL):
    # Set an exception handler:
    try:
        # Build request body.
        body = {"prompt": prompt_workflow}

        # Encode body to process request.
        data = json.dumps(body).encode('utf-8')

        # Process request.
        requests.post(URL, data=data)

    # An error occurs:
    except Exception as e:
        # Print the exception.
        print("[ERROR] " + str(e))

        # Return False if error occurs.
        return None

    # If no error occurs, return True
    return True

def remoteGeneration(prompt, URL, output_folder):
    # Set an exception handler:
    try:
        # Get latest image in folder before generating new one 
        # and storing it in the same folder.
        # This latest image will be the [OLD]_latest_image.
        previous_image = comfyOUT.getLatestImage(output_folder)

        # Call the API to generate the image.
        startRemoteQueue(prompt, URL)

        # Process until the new generated image is stored in output folder.
        while True:
            # Check for latest image.
            latest_image = comfyOUT.getLatestImage(output_folder)
            
            # Check if current latest image correspond to [OLD]_latest_image: 
            if latest_image != previous_image:
                
                # If False, <latest_image> is the new generated image.
                return latest_image 

            # Setting a waiting time to looking for new generated image.
            time.sleep(1)

        # By default return the [OLD]_latest_image.
        return previous_image

    # An error occurs:
    except Exception as e:
        # Print the exception.
        print("[ERROR] " + str(e))

        # Return False if error occurs.
        return None

def webSocketGeneration(prompt_workflow, URL):
    # Set an exception handler:
    try:
        # Get client id using uuid library.
        client_id = str(uuid.uuid4())

        # Create a web socket object.
        ws = websocket.WebSocket()

        # Perform web scoket connection.
        ws.connect("ws://{}/ws?clientId={}".format(URL, client_id))
        
        # Perform request and retrive output.
        images = comfyWS.get_images(ws, prompt_workflow, URL, client_id)

        # Return generated images (1 image for this setup).
        return images

    # An error occurs:
    except Exception as e:
        # Print the exception.
        print("[ERROR] " + str(e))

        # Return False if error occurs.
        return None


