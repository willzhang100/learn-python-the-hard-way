#from the system module import the function argv
from sys import argv

#unpack script and input file name
script, input_file = argv

#define a function that prints all the contents of a file
def print_all(f):
	print f.read()

#define a function that rewinds the file	
def rewind(f):
	f.seek(0)

#define a file that prints a line of the file along with the line number	
def print_a_line(line_count, f):
	print line_count, f.readline()

#variable representing the input file	
current_file = open(input_file)

#printing the whole file
print "First let's print the whole file:\n"

print_all(current_file)

#rewinding the file
print "Now let's rewind, kind of like a tape."

rewind(current_file)

#printing three lines
print "Let's print three lines:"

#set the current line to 1 and print it
current_line = 1
print_a_line(current_line, current_file)

#increment the current line and print it
current_line = current_line + 1
print_a_line(current_line, current_file)

#increment it again and print it
current_line = current_line + 1
print_a_line(current_line, current_file)