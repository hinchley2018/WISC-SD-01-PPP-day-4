fileName = input("Please enter the name of the file you would like to read: ")
myfile = open(fileName, 'r') # Open a file for reading.
contents = myfile.readlines() # Read in the content by line.
myfile.close() # Explicitly close the file
print(contents) #print the contents of the file




# test it on a file that doesn't exist should throw an error
f = FileManipulator("tmp.txt")
print(f.contents)
f.reverse("tmp2.txt")