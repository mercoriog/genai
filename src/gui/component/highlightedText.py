import gradio as gr

def getAvaibleGramentsList(ordered_garments):
    avaible_garments_list = gr.HighlightedText(
        value = ordered_garments,
        label = "Avaible garments:",
        show_label = True,
        interactive = False
    )
    return avaible_garments_list
