import gradio as gr

def getGenderInput():
    gender_input = gr.Radio(
        choices = ["Male", "Female"],
        value = "Male",
        label = "Select gender:",
        interactive = True
    )
    return gender_input

def getHairColorInput():
    hair_color_input = gr.Radio(
        choices = ["Black", "Blonde", "Ginger"], 
        value = "Blonde",
        label = "Select hair color:",
        interactive = True
    )
    return hair_color_input

def getEyesColorInput():
    eyes_color_input = gr.Radio(
        choices = ["Black", "Green", "Blue"],
        value = "Blue",
        label = "Select eyes color:",
        interactive = True
    )
    return eyes_color_input