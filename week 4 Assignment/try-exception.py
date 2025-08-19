filename = input("Enter the filename: ")

try:
	with open(filename, 'r') as file:
		content = file.read()
		print("File content:\n", content)
except FileNotFoundError:
	print("Error: The file does not exist.")
except PermissionError:
	print("Error: You do not have permission to read this file.")
except Exception as e:
	print(f"An unexpected error occurred: {e}")
finally:
	print("Finished processing the file.")