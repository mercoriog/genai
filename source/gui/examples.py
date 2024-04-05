from PIL import Image

# TODO: gestisci l'accesso agli index ed automatizza la creazione degli esempi e l'apertura delle immagini corrispondenti
examples_images = [
    Image.open("genai\\media\\generated_images\\male_blonde_blue_arman1jacket.png"),
    Image.open("genai\\media\\generated_images\\female_blonde_blue_arman1jacket.png"), 
    Image.open("genai\\media\\generated_images\\male_ginger_blue_arman1jacket.png")
]

examples_list = [[
		"Male",
    	"Blonde", 
    	"Blue", 
    	"GIORGIO ARMANI, full body photo of blonde male model wearing dark gray jacket, arman1jacket:1.2, realistic face, extremely high quality RAW photograph, detailed background, intricate, Exquisite details and textures, highly detailed, ultra detailed photograph, warm lighting, 4k, sharp focus, high resolution, detailed skin, detailed eyes, 8k UHD, DSLR, high quality, film grain, Fujifilm XT3, luxury walk in a street of paris", 
    	"(worst quality, greyscale), ac_neg2, zip2d_neg, ziprealism_neg, watermark, username, signature, text, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, bad feet, extra fingers, mutated hands, poorly drawn hands, bad proportions, extra limbs, disfigured, bad anatomy, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, mutated hands, fused fingers, too many fingers, long neck", 
    	examples_images[0]
	],[
    	"Female", 
    	"Blonde", 
    	"Blue", 
    	"GIORGIO ARMANI, full body photo of blonde female model wearing dark gray jacket, arman1jacket:1.2, (realistic face:1.4), extremely high quality RAW photograph, detailed background, intricate, Exquisite details and textures, (highly detailed:1.2), sharp focus, (ultra detailed photograph:1.2), warm lighting, 4k,  high resolution, (detailed skin:1.2), (detailed eyes:1.2), 8k UHD, DSLR, high quality, film grain, Fujifilm XT3, private party, Venice beach in California, summer day, fashion show", 
    	"(worst quality, greyscale), ac_neg2, zip2d_neg, ziprealism_neg, watermark, username, signature, text, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, bad feet, extra fingers, mutated hands, poorly drawn hands, bad proportions, extra limbs, disfigured, bad anatomy, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, mutated hands, fused fingers, too many fingers, long neck, black and white filter", 
    	examples_images[1]
    ],[
	    "Male", 
        "Ginger", 
	    "Blue", 
        "GIORGIO ARMANI, full body photo of ginger male model wearing dark gray jacket, arman1jacket:1.2, realistic face, extremely high quality RAW photograph, detailed background, intricate, Exquisite details and textures, sharp focus, highly detailed, ultra detailed photograph, warm lighting, 4k,  high resolution, detailed skin, detailed eyes, 8k UHD, DSLR, high quality, film grain, Fujifilm XT3, private party on yatch, summer days", 
        "(worst quality, greyscale), ac_neg2, zip2d_neg, ziprealism_neg, watermark, username, signature, text, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, bad feet, extra fingers, mutated hands, poorly drawn hands, bad proportions, extra limbs, disfigured, bad anatomy, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, mutated hands, fused fingers, too many fingers, long neck", 
	    examples_images[2]
    ]]

def getExmaples():
	return examples_list

def getExamplesInfo():
	return len(examples_list)

def getExampleItem(index):
	return examples_list[index]

