# A program that creates and writes into a file 

file = open('bestFile.pdf', 'w')
file.write("This is a test file.")
file.close()

# A program that appends into the bestFile.pdf file
file = open('bestFile.pdf', 'a')
file.write("\nThis is an appended line. Listen to this name Raphael. It will shake the world soon")
file.close()

# A program that reads a file in python
file = open('bestFile.pdf', 'r')
content = file.read()
print(content)