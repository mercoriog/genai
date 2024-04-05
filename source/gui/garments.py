from PIL import Image

#immagini hostate su https://postimg.cc/
garment_images = [
    Image.open("genai\\media\\gallery_images\\arman1jacket.png"),
    Image.open("genai\\media\\gallery_images\\arman1jacket2.png"), 
    Image.open("genai\\media\\gallery_images\\arman1jacket3.png"), 
    Image.open("genai\\media\\gallery_images\\arman1jacket4.png")
]

def getGarmentsList():
	return garment_images

def getGarmentDescription(item_index):
    if item_index == 0:
        item_index = "dark gray jacket, arman1jacket:1.2"
    else: item_index = ""
    return item_index