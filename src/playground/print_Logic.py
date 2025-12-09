# Direct print statement
print("Hello World")
blank_line = ""
print(blank_line)

# Simple variable assignment and print
msg = "Hello World with variable"
print(msg)
print(blank_line)

# Using f-string to format full name
first_name = 'Bart'
last_name = 'Simpson'
full_name = f"{first_name} {last_name}"
print(full_name)
print(blank_line)

# Working with a list of bands
bands = ['Strung Out', 'Rise Against', 'Thrice']
first_band = bands[0]
print(f"My favorite band is {first_band}")
print(blank_line)  

# Accessing the last band using negative indexing   
last_band = bands[-1]
print(f"My least favorite band is {last_band}")
print(blank_line)

# Iterating through the list of bands
for band in bands:
    print(f"I like the band {band}")
print(blank_line)

# Adding new bands to the list
bands.append('Bad Religion')
bands.append('Pennywise')
print("Updated band list:")
for band in bands:
    print(f"- {band}")
print(blank_line)

# Creating a list of squared numbers from 1 to 10
squared_numbers = []
for number in range(1, 11):
    squared_numbers.append(number ** 2)
print("Squared numbers from 1 to 10:")
for squared in squared_numbers:
    print(squared)
print(blank_line)

# Slicing a list of sports
my_sports = ['Football', 'Hockey', 'Soccer']
my_first_two_sports = my_sports[:2]
print("My first two favorite sports are:")

# Making a copy of the sliced list and iterating through it
copy_of_sports = my_first_two_sports[:]
for sport in copy_of_sports:    
    print(sport)
print(blank_line)            

# Working with tuples for sibling information
ages_of_Siblibgs = (41, 39, 37, 26, 21)  # Tuple of sibling ages

names_of_Siblings = ('Shane', 'Cam', 'Ash', 'Saylor', 'Brock')  # Tuple of sibling names

#checking membership in the bands list
is_band= 'Strung Out'
if is_band in bands:
    print(f"{is_band} is in the band list.")    
else:
    print(f"{is_band} is NOT in the band list.")

print(blank_line)

is_band= 'NOFX'
if is_band in bands:
    print(f"{is_band} is in the band list.")    
else:
    print(f"{is_band} is NOT in the band list.")

print(blank_line)

# Final decorative print statements
print(blank_line)
print('************************')
print('** End of Playground ***')
print('************************')
print(blank_line)