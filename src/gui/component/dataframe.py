import gradio as gr

def getPromptMatrix():
	prompt_matrix = gr.Dataframe(
		headers=["Positive prompt index", "Negative prompt index", "Seed index"],
		row_count = (2, 'dynamic'),
		col_count = (3, 'fixed'),
		datatype = ["number", "number", "number"],
		type = "array",
		label = "Insert the prompt index combination and seed index from workflow",
		show_label = True,
		height = 10000,
		interactive = True
	)
	return prompt_matrix

def getCurrentPromptsDataframe(prompt_matrix):
	prompts_dataframe = gr.Dataframe(
		value = prompt_matrix,
		headers=["Positive prompt index", "Negative prompt index", "Seed index"],
		row_count = (2, 'dynamic'),
		col_count = (3, 'fixed'),
		datatype = ["number", "number", "number"],
		type = "array",
		label = "Current prompt index combination and seed index from workflow",
		show_label = True,
		height = 10000,
		interactive = False
	)
	return prompts_dataframe