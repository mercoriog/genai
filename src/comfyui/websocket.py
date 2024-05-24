import websocket #NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import uuid
import json
import urllib.request
import urllib.parse

def queue_prompt(prompt, server_address):
    # Define request body for image generation.
    body = {"prompt": prompt, "client_id": client_id}
    
    # Encode body as json.
    json_body = json.dumps(body).encode('utf-8')
    
    # Build request object.
    request_object =  urllib.request.Request("http://{}/prompt".format(server_address), data=json_body)
    
    # Perform request and read response.
    response_object = json.loads(urllib.request.urlopen(request_object).read())

    # Return response.
    return response_object

def get_image(filename, subfolder, folder_type, server_address):
    # Define request body for image retriving.
    body = {"filename": filename, "subfolder": subfolder, "type": folder_type}
    
    # Encode request body.
    url_values = urllib.parse.urlencode(body)

    # Perform request.
    with urllib.request.urlopen("http://{}/view?{}".format(server_address, url_values)) as response:
        
        # Read and return response.
        return response.read()

def get_history(prompt_id, server_address):
    # Perform history request.
    with urllib.request.urlopen("http://{}/history/{}".format(server_address, prompt_id)) as response:
        
        # Read response and encode as json.
        json_response = json.loads(response.read())

        # Return history encoded as json.
        return json_response

def get_images(ws, prompt, server_address):
    # Get client id with uuid library.
    client_id = str(uuid.uuid4())

    # Perform request.
    generation_response = queue_prompt(prompt, server_address)

    # Get prompt id from generation request.
    prompt_id = generation_response['prompt_id']

    # Initialize output dictionary.
    output_images = {}

    while True:
        # Wait for web socket message.
        out = ws.recv()

        # Check if message is string type.
        if isinstance(out, str):
            # Encode message as json.
            message = json.loads(out)

            # Check value of 'type' key.
            if message['type'] == 'executing':
                # If 'executing' then get 'data' value.
                data = message['data']

                # Check 'node' value and 'prompt id' value from 'data' values 
                if data['node'] is None and data['prompt_id'] == prompt_id:
                    #Execution is done
                    break 
        else:
            # They are binary data.
            continue 

    # When execution is done retrive history.
    history = get_history(prompt_id, server_address)[prompt_id]

    # For each output in history:
    for o in history['outputs']:
        # For each node_id of current output.
        for node_id in history['outputs']:
            # Get node output from current node id.
            node_output = history['outputs'][node_id]

            # Check if node output contains 'images'
            if 'images' in node_output:
                # Then build a generated images list.
                generated_images = []
                # For each image in 'images' key:

                for image in node_output['images']:
                    # Retrive image.
                    image_data = get_image(image['filename'], image['subfolder'], image['type'], server_address)
                    
                    # Add image to generated images list.
                    generated_images.append(image_data)

            # Assign generated images list to output dictionary.
            output_images[node_id] = generated_images

    print("Output images: " + output_images)

    # return generated images dictionary.
    return output_images


