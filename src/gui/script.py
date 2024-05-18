from comfyui import controller as ctrlComfy
from gallery import controller as ctrlGal

# combine user's choices to build the correct one and only positive prompt
def buildPositivePrompt(gender, hair_color, eyes_color, positive_prompt, gallery_item):
    # Get gallery items names.
    gallery_names = ctrlGal.getGalleryNames()
    
    # Build positive prompt with user inputs.
    fixed_positive_prompt = f"full body photo of {hair_color} \
        {gender} model wearing {gallery_names[int(gallery_item)]}:1.2, \
        {eyes_color}:1.2, \
        realistic face, \
        {positive_prompt}"
    
    # Return correct positive prompt.
    return fixed_positive_prompt

def generate(gender, hair_color, eyes_color, positive_prompt, gallery_item, negative_prompt):
	positive_prompt = buildPositivePrompt(gender, hair_color, eyes_color, positive_prompt, gallery_item)
	
	generated_image = ctrlComfy.generateImage(positive_prompt, negative_prompt)

	return generated_image
