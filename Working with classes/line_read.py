# this program reads the contents of the
# philosophers.txt file one line at a time.

def main():
    # open a file named philosophers.txt.
    with open("siblings.txt", "r") as infile:
         # read the three lines from the file
        line1=infile.readline()
        line2=infile.readline()
        # line3=infile.readline()
    
        # removing the newline character
        line1 = line1.rstrip('\n')
        line2 = line2.rstrip('\n')
        print(line1)
        print(line2)
        
        
    
   
    
    
   
    
    
# call the main function
main()