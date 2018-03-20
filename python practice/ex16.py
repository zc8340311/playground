from sys import argv
script, filename=argv

print "we are going to erae %r"% filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit return."

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now Im going to ask you for three lines."

line1=raw_input("line 1: ")
line2=raw_input("line 2: ")
line3=raw_input("line 3: ")

print "Im going to write these to file."

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")
target.write(line3)

print "and finally,we close it."
target.close()
