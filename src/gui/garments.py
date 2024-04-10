from PIL import Image

#immagini hostate su https://postimg.cc/
garment_images = [
    Image.open("genai\\media\\gallery_images\\arman1jacket.png"),
    Image.open("genai\\media\\gallery_images\\arman1jacket2.png"), 
    Image.open("genai\\media\\gallery_images\\arman1jacket3.png"), 
    Image.open("genai\\media\\gallery_images\\arman1jacket4.png")
]

garments_list = [
    "arman1jacket",
    "arman1jacket2",
    "arman1jacket3",
    "arman1jacket4",
]

def getGarmentsList():
    return garments_list

def getGarmentsImagesList():
	return garment_images

def getGarmentDescription(item_index):
    try:
        return garments_list[item_index]
    except:
        return ""