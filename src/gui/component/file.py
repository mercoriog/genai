import gradio as gr

def getWorkflowFile():
	workflow_file = gr.File(
		file_types = ['.json'],
		label = "Upload your ComfyUI workflow API .json file:",
		show_label = True,
		interactive = True
	)
	return workflow_file

def getProvidedWorkflow(file):
	workflow_file = gr.File(
		value = file,
		label = "Provided ComfyUI workflow API .json file:",
		show_label = True,
		interactive = False
	)
	return workflow_file