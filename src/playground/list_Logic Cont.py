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

#------------------------------------
#start of lists_Logic playground
#----------------------------------

#check if current moduule is example
lists_logic_cont_example = True
    
if lists_logic_cont_example:
    print("This begins the lists logic cont example.")
else:
    print("Maybe the end of examples.")  

print(blank_line) 

#####################################
####  end of boilerplate code  ####
#####################################

first_team = ""
second_team = ""
third_team = ""
fourth_team = "" 
last_team = ""

#define a list of teams
teams = ["Bucs", "Rams", "Lions", "Giants"]
#------------------------------------ 

#accessing elements in the list
def setup_teams():
    if print_on:
        print("Setting up teams list...")
    else:
        print("Teams setup skipped.")
    print(blank_line) 

    global first_team, second_team, third_team, fourth_team, last_team

    #since we making this a function, we need to...
    #  accomodate remove + pop scenarios
    if len(teams) > 0:
        first_team = teams[0]
    else:
        first_team = "None"
    if len(teams) > 1:
        second_team = teams[1] 
    else:
        second_team = "None"
    if len(teams) > 2:
        third_team = teams[2]
    else:
        third_team = "None"
    if len(teams) > 3:
        fourth_team = teams[3]  
    else:
        fourth_team = "None"


    #getting the last team using negative indexing
    if len(teams) > 0:
        last_team = teams[-1]
    else:
        last_team = "None"
#------------------------------------ 

#displaying the team setup
def print_teams():

    if print_on:
        print(f"The first team is: {first_team}")
        print(f"The second team is: {second_team}")
        print(f"The third team is: {third_team}")
        print(f"The fourth team is: {fourth_team}")
        print(f"The last team using negative indexing is: {last_team}")
        print(blank_line)
#------------------------------------ 

print("After creating teams list:") 
setup_teams()
print_teams()

#modifying the list by adding new teams
teams[2] = "Packers"  #changing the third team
teams[3] = "Bears"    #changing the fourth team

print("After modifying the teams list:")    
setup_teams()
print_teams()

#adding to end of the list using append
teams.append("Vikings")  #adding a new team at the end
print("After appending a new team to the list:")
setup_teams()
print_teams()

#create a list using append
#we make this a function to reuse in this playground
def create_nfc_south():
    if print_on:
        print("Creating NFC South teams list using append...")
    else:
        print("NFC South teams setup skipped.")
    print(blank_line)

    global teams
    teams = []  #start with an empty list
    teams.append("Falcons")
    teams.append("Saints")
    teams.append("Panthers")
    teams.append("Buccaneers")
#------------------------------------ 


print("After creating a new teams list using append:")
create_nfc_south()
setup_teams()
print_teams()   
     
#inserting an element at a specific position
teams.insert(1, "Cowboys")  #inserting at index 1
teams.insert(4, "Eagles")   #inserting at index 4
print("After inserting a new team at index 1 and 4:")
setup_teams()
print_teams()

#removing an element from the list by its item value
teams.remove("Saints")  #removing "Saints" from the list
print("After removing 'Saints' from the list:")
setup_teams()
print_teams()

#removing an element from the list by its index with del
del teams[0]  #removing the team at index 0
print("After deleting the team at index 0:")
setup_teams()
print_teams()

#------------------------------------  

#reset the teams list to original for further operations
#we make this a function to reuse in this playground
def reset_teams():
    if print_on:
        print("Resetting teams list to original NFC South teams...")
    else:
        print("Teams reset skipped.")
    print(blank_line)

    global teams
    create_nfc_south()
    setup_teams()
    print_teams()


#pop last element from the list by its index
removed_team = teams.pop()  #removing the last team  
print(f"After removing the last team ({removed_team}):")
setup_teams()
print_teams()

#pop first element from the list by its index
removed_team = teams.pop(0)  #removing the first team
print(f"After removing the first team ({removed_team}):")
setup_teams()
print_teams()

#determine the length of the list
num_of_teams = len(teams)
print(f"Number of teams remaining in the list: {num_of_teams}")

#------------------------------------  
reset_teams()  #reset teams list before sorting

#sorting the list permanently in alphabetical order
teams.sort() 
print("After sorting the teams list in alphabetical order:")
setup_teams()
print_teams()

#sorting the list permanently in reverse alphabetical order
teams.sort(reverse=True)
print("After sorting the teams list in reverse alphabetical order:")
setup_teams()
print_teams()   

#sorting a list temporarily using sorted()
sorted_teams = sorted(teams)
print("After temporarily sorting the teams list in alphabetical order:")
setup_teams()
print_teams()
print(f"Temporarily sorted teams: {sorted_teams}")

#reversing the order of the list
sorted_teams_reverse = sorted(teams, reverse=True)
print("After temporarily sorting the teams list in reverse alphabetical order:")
setup_teams()
print_teams()
print(f"Temporarily sorted teams in reverse order: {sorted_teams_reverse}")


#reverse the order of list with reverse()
teams.reverse()
print("After reversing the order of the teams list:")
setup_teams()
print_teams()
#------------------------------------ 

#printing all items in a list using a loop
print("Printing all teams in the list using a loop:")
for team in teams:
    print(team)

#printing a message for each item and a separator msg after
print(blank_line)
print("Printing each team with a message:")
for team in teams:
    print(f"Team: {team}")
    print("----------")

print("\nEnd of lists logic example.")

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

#####################################
####  reference section          ####
#####################################

#The range() function
#You can use the range() function to work with a set of...
# numbers efficiently. The range() function starts at 0 by...
# default, and stops one number below the number passed to...
# it. You can use the list() function to efficiently...
# generate a large list of numbers.

#Simple statistics
#There are a number of simple statistical operations you can...
# run on a list containing numerical data.

#Slicing a list
#You can work with any subset of elements from a list. A...
# portion of a list is called a slice. To slice a list...
# start with the index of the first item you want, then add...
# a colon and the index after the last item you want. Leave...
# off the first index to start at the beginning of the list,
# and leave off the second index to slice through the end of
# the list.

#Copying a list
#To copy a list make a slice that starts at the first item...
# and ends at the last item. If you try to copy a list...
# without using this approach, whatever you do to the copied
# list will affect the original list as well.



#####################################
####  end of reference           ####
#####################################