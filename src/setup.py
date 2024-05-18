from controller import env_controller as envc

def setup():
	# Check for environment.
	env = envc.checkEnv()

	# If environment NOT found:
	if not env:
		# Notify environment NOT found.
		print("[SETUP] Environment not found.")

		# Load environment.
		env = envc.initEnv()
		
		# Check if env is loaded:
		if not env:
			# Notify error in loading.
			print("[SETUP] Error in load environment.")	
		else:
			# Notify environment correctly loaded.	
			print("[SETUP] Environment loaded with no errors.")
	else:
		# Notify environment found.
		print("[SETUP] Environment found.")

	# End void function.
	return

if __name__ == "__main__":
	# Start setup.
	setup()