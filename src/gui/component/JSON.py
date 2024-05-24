import gradio as gr

def getWorkflowJSON(json_data):
	workflow_json = gr.JSON(
		value = json_data,
		label = "Current workflow:",
		show_label = True
	)
	return workflow_json