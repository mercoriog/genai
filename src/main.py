from gui import builder

if __name__ == "__main__":
	# Build GUI.
	demo = builder.buildGUI()

	# Launch GUI.
	demo.launch(share = False)
