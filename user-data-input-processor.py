#Task 1: Input Length Validator 
# Write a script that asks for and checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

while True:   # set an initial loop to ask user to enter first and last name
    first_name = input("Please enter your first name: ")
    second_name = input("Please enter you second name: ") 
    
    if len(first_name) >= 2 and  len(second_name) >= 2:    # if the length of first and second name are greater than 2
        print(f"It's very nice to meet you {first_name} {second_name}!") 
        break
    else:   # if either first or second name are less than 2 characters, print error and ask user to input again 
        print("Error! Length of first and last name must be greater than 2 characters.") 
        
