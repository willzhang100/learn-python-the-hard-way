"""
#import the function argv from the sys module
from sys import argv

#unpack the script and filename from argv
script, filename = argv

#inform the user that you will erase [filename]
print "We're going to erase %r. " % filename
print "If you don't want that, hit CTRL-C (^C). "
print "If you do want that, hit RETURN."

#user enters a prompt
raw_input("?")

#opens the file, loads it to target, and sets the mode to 'write'
print "Opening the file..."
target = open(filename, 'w')

#truncates the target file (erases)
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#prompts the user to enter 3 lines
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#writes the three lines to the file, appending a newline after every line
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#closes the file for good practice
print "And finally, we close it."
target.close()
"""

#use read and argv
filename = raw_input("What is the name of your file? ")

print "We are now going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C). "
print "If you do want that, hit RETURN."

raw_input("?")

print "Erasing %r ..." % filename
target = open(filename, 'w')
#target.truncate()

print "Now I will ask you for three lines: "
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

#with just one write
target.write(("%s\n%s\n%s\n") % (line1, line2, line3))
"""
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""
print "Now I will close the file"
target.close()

