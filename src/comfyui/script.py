from comfyui import websocket as comfyWS
import websocket #NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import uuid

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


