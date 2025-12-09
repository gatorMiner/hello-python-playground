#global variable to control printing
print_on = False
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

# Direct print statement
if print_on:
    print("Hello World")
    print(blank_line)

# Simple variable assignment and print
msg = "Hello World with variable"
if print_on:
    print(msg)
    print(blank_line)

# Using f-string to format full name
first_name = 'Bart'
last_name = 'Simpson'
full_name = f"{first_name} {last_name}"

if print_on:
    print(full_name)
    print(blank_line)

# Working with a list of bands
bands = ['Strung Out', 'Rise Against', 'Thrice']
first_band = bands[0]

if print_on:
    print(f"My favorite band is {first_band}")
    print(blank_line)  

# Accessing the last band using negative indexing   
last_band = bands[-1]
if print_on:
    print(f"My least favorite band is {last_band}")
    print(blank_line)

# Iterating through the list of bands
if print_on:
    for band in bands:
        print(f"I like the band {band}")
    print(blank_line)

# Adding new bands to the list
bands.append('Bad Religion')
bands.append('Pennywise')
if print_on:
    print("Updated band list:")
    for band in bands:
        print(f"- {band}")
    print(blank_line)

# Creating a list of squared numbers from 1 to 10
squared_numbers = []
for number in range(1, 11):
    squared_numbers.append(number ** 2)
if print_on:
    print("Squared numbers from 1 to 10:")
    for squared in squared_numbers:
        print(squared)
    print(blank_line)

# Slicing a list of sports
my_sports = ['Football', 'Hockey', 'Soccer']
my_first_two_sports = my_sports[:2]

if print_on:
    print("My first two favorite sports are:")

# Making a copy of the sliced list and iterating through it
copy_of_sports = my_first_two_sports[:]
if print_on:
    for sport in copy_of_sports:    
        print(sport)
    print(blank_line)            

# Working with tuples for sibling information
ages_of_Siblings = (41, 39, 37, 26, 21)  # Tuple of sibling ages

names_of_Siblings = ('Shane', 'Cam', 'Ash', 'Saylor', 'Brock')  # Tuple of sibling names

#checking membership in the bands list

is_band= 'Strung Out'

if print_on:
    if is_band in bands:
        print(f"{is_band} is in the band list.")    
    else:
        print(f"{is_band} is NOT in the band list.")
    print(blank_line)

is_band= 'NOFX'

if print_on:
    if is_band in bands:
        print(f"{is_band} is in the band list.")    
    else:
        print(f"{is_band} is NOT in the band list.")
    print(blank_line)


#------------------------------------
#start of if conditions playground
#------------------------------------

#check if printing is enabled using boolean variable
conditional_logic_example = True

if conditional_logic_example:
    print("This begins the conditional logic example.")
else:
    print("Maybe the end of examples.")  

print(blank_line) 

#check voting eligibility for user_age
vote_age = 18
user_age = 20
print(f"User age is: {user_age}")
if user_age >= vote_age:
    print("User is eligible to vote.")    
else:
    print("User is not eligible to vote.")
print(blank_line)

#using if-elif-else to determine ticket price based on age
ticket_price_infant = 0
ticket_price_child = 25 
ticket_price_adult = 40
ticket_price_senior = 30    
ticket_age_limit_child = 4
ticket_age_limit_adult = 18
ticket_age_limit_senior = 65

if user_age < ticket_age_limit_child:
    ticket_price = ticket_price_infant
elif user_age < ticket_age_limit_adult:
    ticket_price = ticket_price_child
elif user_age < ticket_age_limit_senior:
    ticket_price = ticket_price_adult
else:
    ticket_price = ticket_price_senior

print(f"Ticket price is: ${ticket_price}")
print(blank_line)  

#start of dictionary and loop example
#create the dictionary
fantasy_football_team = { 'name': 'The Stonecutters'
                         ,'manager': 'Bart Simpson'
                         ,'points': 1250
                         ,'rank': 3}

print(f"{fantasy_football_team['name']} team...")
print(f"is managed by {fantasy_football_team['manager']}.")
print(blank_line)  

#for loop to iterate through all key-value pairs
#in the dictionary
print("Team details (loop thru all key-value pairs):")
for key, value in fantasy_football_team.items():
    print(f"{key}: {value}")
print(blank_line)

#adding new key-value pair to the dictionary
print("Adding new key-val pair, email to team details...")
fantasy_football_team['email'] = "bart.simpson@example.com"

#for loop to iterate through all key-value pairs 
#in the dictionary again to display new key-value pair
print("Team details (loop thru all key-value pairs):")
for key, value in fantasy_football_team.items():
    print(f"{key}: {value}")
print(blank_line)

#for loop to iterate through keys only
print("Team details (loop thru keys only):")
for key in fantasy_football_team.keys():
    print(f"{key} is a key in the dictionary.")
print(blank_line)

#for loop to iterate through values only
print("Team details (loop thru values only):")
for value in fantasy_football_team.values():
    print(f"{value} is a value in the dictionary.")
print(blank_line)   

# Final decorative print statements
print(blank_line)
print('************************')
print('***** END of Play  *****')
print('************************')
print(blank_line)