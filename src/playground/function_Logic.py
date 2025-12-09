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
#start of function_Logic playground
#------------------------------------

#check if printing is enabled using boolean variable
function_logic_example = True
    
if function_logic_example:
    print("This begins the function logic example.")
else:
    print("Maybe the end of examples.")  

print(blank_line) 

#####################################
####  end of boilerplate code  ####
#####################################

#a simple function to demonstrate function logic
def greet_user():
    """Function to greet the user."""
    if print_on:
        print("Hello from inside the greet_user function!")
        print(blank_line)

greet_user()
#------------------------------------

#passing an argument to a function  
def greet_user_argument(user_name):
    """Function to greet the user with their name."""
    if print_on:
        print(f"Hello, {user_name}, from function!")
        print(blank_line)

greet_user_argument("Alice")
#------------------------------------    

#default values for function parameters 
def make_burger(topping_1="lettuce", topping_2="tomato"):
    """Function to make a burger with given toppings."""
    if print_on:
        print("Making a burger with the following toppings:")
        print(f"- {topping_1}")
        print(f"- {topping_2}")
        print(blank_line)

make_burger()
if print_on:
    print("Making a burger with 1 custom topping...")
make_burger("bacon")

if print_on:
    print("Making a burger with 2 custom toppings...")
make_burger("bacon", "cheese")
#------------------------------------

#returning a value from a function
def add_numbers(num1, num2):
    """Function to add two numbers and return the result."""
    result = num1 + num2
    return result

sum_result = add_numbers(5, 7)
if print_on:
    print(f"The sum of 5 and 7 is: {sum_result}")
    print(blank_line)          
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