# Set a variable for the txt file that we are reading from.
input_file_name = "data.txt"

"""
A function that reads a text file containing bank customer info and
converting the strings into a list of customers through for loop.

Parameters:
    input_file_name (string): (filepath) txt file that we are reading from.

Returns:
    list: append each line one by one after removing the newline using replace and
    converting the string into a List using split.
"""
def load_data(input_file_name):
    infile = open(input_file_name, "r")
    lines = infile.readlines()
    # Created an empty list to append the line list to.
    # This will allow us to access the specific List elements later in other functions.
    customer_info = []
    for line in lines:
        customer_info.append(line.replace("\n","").split(","))
    return customer_info

customer_info = load_data(input_file_name)

# username = input("Please enter your User Name: ")
# password = input("Please enter your Password: ")

"""
A function to check if the username and password entered match with the
respective (list access) customer_info list elements through for loop.

Parameters:
    username (string): the username customer enetered
    password (string): the password customer enetered

Returns:
    bool: if the username and password match
    with the respective (list access) customer_info list element through for loop then return True.
"""
def do_username_password_match(username, password):
    for customer in customer_info:
        if customer[0] == username and customer[1] == password:
            return True

"""
A function to display full naem and account balance if the username and password entered match with the respective (list access) customer_info list elements 
through for loop.

Parameters: 
    username (string): the username customer enetered
    password (string): the password customer enetered

Returns:
    string: if the username and password match 
    with the respective (list access) customer_info list element through for loop then return full name and amount balance.
"""

def display_customer_info(username, password):
    for customer in customer_info:
        if customer[0] == username and customer[1] == password:
            return f"Full Name: {customer[2]}\nAccount Balance: {customer[3]}"
"""
A function to prompt the user for username and password input and ask for input again using while loop if the 
password username do not match and if the incorrect login attempt increase the number of allowed login attempt.

Returns:
    string: if match is true display the accoutn info by calling the display function and display the error message if it is not.
"""
def balance_check():
    print("Welcome to the Balance-Check App!\n")
    allowed_login_attempts = 3
    login_attempts = 0
    while True:
        username = input("Please enter your User Name: ")
        password = input("Please enter your Password: ")
        match = do_username_password_match(username, password)
        if match is True:
            print(f"{display_customer_info(username, password)}\n")
            return display_customer_info(username, password)
        elif match is not True:
            print("Username or Password do not match!!\n")
            login_attempts += 1
            if login_attempts == allowed_login_attempts:
                print("There are too many wrong entries, please reach us for further assistance or re-open the app.\n")
                break

# function to start the app
load_data(input_file_name)
balance_check()