"""
#from the sys module import the function argv
from sys import argv
#from the os.path module import the function exists
from os.path import exists

#unpack argv into script, from_file, to_file
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#open the file you are copying from
in_file = open(from_file)
#read from that file and store it
indata = in_file.read()

#writes how many bytes the input file is
print "The input file is %d bytes long" % len(indata)

#prints whether the output file exists
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#opens the output file and sets the mode to 'write'
out_file = open(to_file, 'w')
#writes the contents of the input file to the output file
out_file.write(indata)

print "All done"

in_file.close()
out_file.close()
"""

from sys import argv

script, in_file, out_file = argv
print "Writing...", open(out_file, 'w').write(open(in_file).read())
print "All done."