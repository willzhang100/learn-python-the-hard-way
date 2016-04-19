#import the function argv from the sys module
from sys import argv
"""
#unpack the contents of argv into the script and filename
script, filename = argv

#open the file specified by the filename
txt = open(filename)

#print the filename
print "Here's your file %r: " % filename
#print the contents of the file
print txt.read()
"""
#ask for the filename again
print "Type the filename again: "
#write down the filename
file_again = raw_input("> ")

#open the file specified by the filename
txt_again = open(file_again)

#print the contents of the file
print txt_again.read()
txt_again.close()
