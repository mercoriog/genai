import gradio as gr

def getItemsGallery(gallery_images):
    items_gallery = gr.Gallery(
        value = gallery_images,
        format = "png",
        label = "Select garment:", 
        show_label = True,
        min_width = 512,
        columns = 4,
        height = 512,
        allow_preview = True,
        interactive = False
    )
    return items_gallery













