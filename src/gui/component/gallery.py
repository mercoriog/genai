import gradio as gr

def getItemsGallery(gallery_images):
    items_gallery = gr.Gallery(
        value = gallery_images,
        format = "png",
        label = "Select garment:", 
        show_label = True, 
        min_width = 512,
        height = 512, 
        allow_preview = True,
        interactive = True
    )
    return items_gallery













