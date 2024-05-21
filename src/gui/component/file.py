import gradio as gr

def getWorkflowFile():
	workflow_file = gr.File(
		file_types = ['.json'],
		label = "ComfyUI workflow API .json file:",
		show_label = True,
		interactive = True
	)
	return workflow_file