# fileName = input("Please enter the name of the file you would like to read: ")
# myfile = open(fileName, 'r') # Open a file for reading.
# contents = myfile.readlines() # Read in the content by line.
# myfile.close() # Explicitly close the file
# print(contents) #print the contents of the file

class FileManipulator:
    def __init__(self, fileName):
        self.contents = None
        #try until we have contents
        while self.contents == None:
            try:
                myfile = open(fileName, 'r')
                self.contents = myfile.readlines()
            #handle various file exceptions
            except (FileNotFoundError, TypeError, OSError) as e:
                #debg
                print(type(e), e)
                # prompt again
                fileName = input("Please enter a valid file name")
    def reverse(self, fileName):
        
        #open file for writing
        try: 
            myfile = open(fileName, 'w')
            #:-1 give me all contents
            #::-1 reverse the contents
            reversed_contents = [x.strip()[::-1] for x in self.contents]
            print("reversed",reversed_contents)
            for i in range(len(reversed_contents)):
                #try writing the file
                # the last line
                if (i == len(reversed_contents) - 1):
                    myfile.write(reversed_contents[i])
                else:
                    myfile.write(reversed_contents[i] + '\n')
        except (FileNotFoundError, TypeError, OSError) as e:
            #debg
            print(type(e), e)
            # prompt again
            fileName = input("Please enter a valid file name")            
        finally:
            myfile.close()

    def upper(self, fileName):
        try:
            myfile = open(fileName, 'w')
            upper_contents = [x.strip().upper() for x in self.contents]
            for i in range(len(upper_contents)):
                myfile.write(upper_contents[i]+'\n')
        except (FileNotFoundError, TypeError, OSError) as e:
            print(type(e),e)
            fileName = input("Please enter a valid file name: ")
        finally:
            myfile.close()
# test it on a file that doesn't exist should throw an error
f = FileManipulator("tmp.txt")
print(f.contents)
f.reverse("tmp-reversed.txt")
f.upper("tmp-upper.txt")