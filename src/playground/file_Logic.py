#global variable to control printing
print_on = True
blank_line = ""


# Final decorative print statements
print(blank_line)
print('************************')
print('**** START of Play  ****')
print('************************')
print(blank_line)


#check if printing is enabled using boolean variable
if print_on:
    print("Printing is enabled.")
else:
    print("Printing is disabled.")  
print(blank_line) 

#####################################
####   end of boilerplate code   ####
#####################################

#### Working with files ####
#Your programs can read from files and write to files. 
#The pathlib library makes it easier to work with files... 
# and directories. Once you have a path defined, you can work...
# with the read_text() and write_text() methods.

#The read_text() method reads in the entire contents of a file.
#You can then split the text into a list of individual lines,...
# and then process each line as you need to.

#### Exceptions ####
#Exceptions help you respond appropriately to errors that are...
# likely to occur. 
#You place code that might cause an error in the try block.
#Code that should run in response to an error goes in the...
# except block. 
#Code that should run only if the try block was successful... 
# goes in the else block.

#####################################
####  start of boilerplate code  ####
#####################################

#------------------------------------
#start of files_Logic playground
#------------------------------------

#check if printing is enabled using boolean variable
file_logic_example = True
    
if file_logic_example:
    print("This begins the file logic example.")
else:
    print("Maybe the end of examples.")  

print(blank_line) 

#####################################
####  end of boilerplate code  ####
#####################################


#read the contents of a file
from pathlib import Path
read_File_Name = 'readFileSample.txt'

#function to read and display file contents
def display_file_contents(file_name):
    if print_on:
        print(f"Reading from file '{file_name}':")
        print(blank_line)

    # define the file path
    file_path = Path(file_name)
    contents = file_path.read_text()
    lines = contents.splitlines()   

    #print each line from the file
    def print_lines():
        if print_on:
            for line in lines:
                print(line)
            print(blank_line) 
    print_lines()

#call the function to read and display the file contents
display_file_contents(read_File_Name)    

#------------------------------------ 

#write to a file 
write_File_Name = 'writeFileSample.txt'

if print_on:
    print(f"Writing to file '{write_File_Name}':")
    print(blank_line)

file_path = Path(write_File_Name)
msg = "This is a new line added to the file"
file_path.write_text(msg)

if print_on:
    print("New contents of the file after writing:")
    print(blank_line)

#call the function to read and display the file contents
display_file_contents(write_File_Name)  


#------------------------------------
#start of exception_Logic playground
#------------------------------------

#check if printing is enabled using boolean variable
exception_logic_example = True
    
if exception_logic_example:
    print("This begins the exception logic example.")
else:
    print("Maybe the end of examples.")  

print(blank_line) 


#catching an exception example
prompt = "How many slices of pizza do you want? "
num_slices = input(prompt)

try:
    num_slices = int(num_slices)
except ValueError:
    print("Please enter a valid number.")
else:
    if print_on:
        print(f"Okay, you want {num_slices} slices of pizza.")  
     
#------------------------------------ 
   

#####################################
####  start of boilerplate code  ####
#####################################

#>>boiler plate block of code 
     
#------------------------------------  

# Final decorative print statements
print(blank_line)
print('************************')
print('***** END of Play  *****')
print('************************')
print(blank_line)