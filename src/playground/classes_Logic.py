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

#>>>>>  maybe custom code  <<<<<

#####################################
####  start of boilerplate code  ####
#####################################

#------------------------------------
#start of classes_Logic playground
#------------------------------------

#check if printing is enabled using boolean variable
classes_logic_example = True
    
if classes_logic_example:
    print("This begins the classes logic example.")
else:
    print("Maybe the end of examples.")  

print(blank_line) 

#####################################
####  end of boilerplate code  ####
#####################################

#A class defines the behavior of an object and...
# the kind of information an object can store. 
#The information in a class is stored in attributes,... 
# and functions that belong to a class are called methods. 
#A child class inherits the attributes and methods from its parent class.

#creating a dog class
class Dog:
    """Represent a dog."""
    
    def __init__(self, name):
        """Initialize dog object."""
        self.name = name
        
    def sit(self):
        """Simulate sitting."""
        if print_on:
            print(f"{self.name} is sitting.")
            print(blank_line)

my_dog = Dog('Peso')

if print_on:
    print(f"{my_dog.name} is a great dog!")
    print(blank_line) 
    
my_dog.sit()
#------------------------------------

#>>use inheritance to create a dog class
class SARDog(Dog):
    """Represent a search and rescue dog."""
    
    def __init__(self, name):
        """Initialize search and rescue dog object."""
        super().__init__(name)
        
    def search(self):
        """Simulate searching."""
        if print_on:
            print(f"{self.name} is searching.")
            print(blank_line)

my_sar_dog = SARDog('Willie')

if print_on:
    print(f"{my_sar_dog.name} is a search and rescue dog!")
    print(blank_line)
    
my_sar_dog.sit()
my_sar_dog.search() 
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