# Import prettytable to display a beautiful inventory table
from prettytable import PrettyTable


# CONSTANTS section
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = '\033[0m'
LIGHTGRAY  = "\033[37m"

TITLE = f'''{LIGHTGRAY}
███████╗██╗  ██╗ ██████╗ ███████╗    ██╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗████████╗ ██████╗ ██████╗ ██╗   ██╗
██╔════╝██║  ██║██╔═══██╗██╔════╝    ██║████╗  ██║██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
███████╗███████║██║   ██║█████╗      ██║██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝ ╚████╔╝ 
╚════██║██╔══██║██║   ██║██╔══╝      ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝  
███████║██║  ██║╚██████╔╝███████╗    ██║██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║   ██║   
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝ {RESET}'''


#========The beginning of the class==========
class Shoe:
    # constructor to set the country, code, product, cost and quantity
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    # Return the cost of a shoe object
    def get_cost(self):
        return int(self.cost)


    # Return the quantity of a shoe object
    def get_quantity(self):
        return int(self.quantity)


    # Return a string for the detail of a shoe object
    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


#=============Shoe list===========
# Define a variable list that will be used to store a list of shoes objects
shoe_list = []

#==========Functions outside the class==============

# This function will read data from the inventory.txt, each line in inventory file represent a shoe object
# Create a shoe object per each line and add it to the shoe_list
def read_shoes_data():
    # Use error handling for opening the inventory.txt file, if file does not exist, display message to user
    try:
        with open("inventory.txt", "r") as f:
            contents = f.readlines()
            # Loop through all lines in the file except the first header line, create and add shoe ojects to shoe_list
            for i in range(1, len(contents)):
                contents[i] = contents[i].strip('\n').split(',')
                shoe = Shoe(contents[i][0], contents[i][1], contents[i][2], int(contents[i][3]), int(contents[i][4]) )
                shoe_list.append(shoe)

    except FileNotFoundError:
        print(f"{RED}File inventory.txt does not exist!{RESET}")


# This function will take a shoe code, loop through shoe code of all shoes in shoe_list, return if it is exist or not
def check_code_exist(code):
    is_code_exist = False
    for shoe in shoe_list:
        if shoe.code == code:
            is_code_exist = True
    return is_code_exist


# This function captures all required data to create a shoe oject, create the shoe object, append it to the shoe_list
def capture_shoes():
    # Ask user to enter country and shoe code
    country = input("Please enter the country of a shoe: ")
    shoe_code = input("Please enter the shoe code: ")

    # Assume shoe code is an primary key, ask user until they enter a non exist key
    is_duplicate_code = check_code_exist(shoe_code)
    while is_duplicate_code:
        shoe_code = input(f"The shoe code {RED}'{shoe_code}'{RESET} already exist, please enter a new shoe code: ")
        is_duplicate_code = check_code_exist(shoe_code)

    # Ask user to enter shoe description
    product = input("Pleaes enter the product description: ")

    # Ask user for the cost of the shoe
    cost = -1
    try:
        cost = int(input("Please enter a positive number for the cost: "))
    except ValueError:
        # Display error message if user input nat a number
        print(f"{RED}Not a number.  Try again...{RESET}")

    # Use while loop to ask user to enter a valid cost for a shoe
    # Assume zero or above is a valid input for the cost, display an error message if use enter a number below zero
    while cost < 0:
        try:
            cost = int(input(f"{RED}Not a valid cost, pleases enter a positive "
                             f"number for the cost again: {RESET}"))
        except ValueError:
            print(f"{RED}Not a number.  Try again...{RESET}")

    # Ask user for the quantitiy of the shoe
    quantity = -1
    try:
        quantity = int(input("Please enter a positive number for the quantity: "))
    except ValueError:
        # Display error message if user input not a number
        print(f"{RED}Not a number.  Try again...{RESET}")

    # Use while loop to ask user to enter a valid quantity for a shoe
    # Assume zero or above is a valid input for the quantity, display an error message if use enter a number below zero
    while quantity < 0:
        try:
            quantity = int(input(f"{RED}Not a valid quantity, pleases enter a positive "
                                 f"number for the quantity again: {RESET}"))
        except ValueError:
            print(f"{RED}Not a number.  Try again...{RESET}")

    # Create a shoe object and add it to the shoe_list
    shoe = Shoe(country, shoe_code, product, cost, quantity)
    shoe_list.append(shoe)

    # Append the new shoe to the inventory.txt file
    with open("inventory.txt", "a") as f:
        f.write(f"\n{country},{shoe_code},{product},{str(cost)},{str(quantity)}")


# This function display a shoe detail, it take shoe code and display the detail of that particular shoe object
def display_shoe_detail(code):
    is_shoe_found = False
    # lookup the shoe in the shoe_list and display it detail
    for shoe in shoe_list:
        if shoe.code == code:
            is_shoe_found = True
            output = "\n-------------- Shoe Detail --------------\n"
            output += f"Country :       {shoe.country}\n"
            output += f"Code    :       {shoe.code}\n"
            output += f"Product :       {shoe.product}\n"
            output += f"Cost    :       {shoe.cost}\n"
            output += f"Quantity:       {shoe.quantity}\n"
            output += "-----------------------------------------"
            print(output)

    # If coundn't find the shoe, display error message to user
    if not is_shoe_found:
        print(f"\n{RED}Could not find shoe code '{code}'!{RESET}")


# This function use the prettytable module to print the shoe table,
# It loops through all shoes in the shoe_list to add each shoe object to the table before printing table
def view_all():
    table = PrettyTable()
    # Create column headers
    table.field_names = ["COUNTRY", "CODE", "PRODUCT", "COST", "QUANTITY"]

    # Loop through the shoe_list to add each shoe object to the table before printing
    for shoe in shoe_list:
        table.add_row(shoe.__str__().split(','))
    print(table)


# This is finding the lowest quantitiy of shoe in shoe_list, check if re-stock is needed, if yes, update the quantity
def re_stock():
    # Create a new list with two shoe data, quantity and shoe code
    list = [[int(shoe.quantity), shoe.code] for shoe in shoe_list]

    # sort the quantitiy with ascending order, display the first element in ordder to show the lowest quantity of shoe
    list.sort()
    current_code = (list[0][1])
    display_shoe_detail(current_code)

    # Ask user if they want to re-stock
    choice = input(f"{GREEN}The above shoe has the lowest quantity, "
                   f"do you want to add quantity {BLUE}(Y/N){RESET}? ").lower()
    while choice != "n":
        if choice == "y":
            # Ask user for the adding quantity
            quantity = -1
            try:
                quantity = int(input("Please enter a positive number for the adding quantity: "))
            except ValueError:
                # Display error message if user input not a number
                print(f"{RED}Not a number.  Try again...{RESET}")

            # Use while loop to ask user to enter a valid quantity for a shoe
            # Assume zero or above is a valid input, display an error message if use enter a number below zero
            while quantity < 0:
                try:
                    quantity = int(input(f"{RED}Not a valid quantity, "
                                         f"pleases enter a positive number for the quantity again: {RESET}"))
                except ValueError:
                    print(f"{RED}Not a number.  Try again...{RESET}")

            # Update the shoe_list and invetory.txt file with new quantity
            for shoe in shoe_list:
                if shoe.code == current_code:
                    line_replace_from = f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}"
                    line_replace_to = f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost}," \
                                      f"{shoe.get_quantity() + quantity}"
                    # Update the quantity of the shoe object
                    shoe.quantity = shoe.get_quantity() + quantity
            # Read content from inventory.txt file
            with open("inventory.txt", "r") as f:
                # Replace the content with updated quantity
                contents = f.read().replace(line_replace_from, line_replace_to)

            # Write the new content to the inventory.txt
            with open("inventory.txt", "w") as f:
                f.write(contents)
            print(f"{GREEN}Quantitiy updated accordingly{RESET}")
            break
        else:
            choice = input(f"{RED} '{choice}'{RESET}is not a valid choice, please enter {BLUE}(Y/N){RESET}: ").lower()


# This function ask user for a shoe code, display its detail if found
def search_shoe():
    shoe_code = input("Please enter the shoe code: ")
    display_shoe_detail(shoe_code)


# This function use the prettytable module to print the shoe table with its value
# It loops through all shoes in the shoe_list to add each shoe object with calculated value to the table
def value_per_item():
    table = PrettyTable()
    total_value = 0
    # Create column headers
    table.field_names = ["COUNTRY", "CODE", "PRODUCT", "COST", "QUANTITY", "VALUE"]

    # Loop through the shoe_list, calculate value for each shoe, and add each shoe object to the table before printing
    for shoe in shoe_list:
        value = shoe.get_quantity() * shoe.get_cost()
        total_value += value
        line = shoe.__str__().split(',')
        line.append(str(value))
        table.add_row(line)
    print(table)

    # Display the total value of all shoe as well
    print(f"{GREEN}The total value of all shoes is: {total_value}{RESET}")


# The function is finding the highest quantitiy of shoe in shoe list, print it detail and print it as being for sale
def highest_qty():
    # Create a new list with two shoe data, quantity and code
    list = [[int(shoe.quantity), shoe.code] for shoe in shoe_list]

    # sort the quantitiy with ascending order, show the last shoe for the highest quantity with being for sale message
    list.sort()
    display_shoe_detail(list[-1][1])
    print(f"{GREEN}The above shoe has the highest quantity, this shoe as being for sale{RESET} ")


#==========Main Menu=============

# Load all shoe data file the inventory.txt file to the shoe_list
read_shoes_data()

user_option = ""
print(TITLE)

# Use while loop to display a main menu for user to choose an option
while user_option != "exit":
    user_option = input(f"\nPlease select an option: {BLUE}capture_shoes{RESET}/{BLUE}view_all{RESET}/"
                        f"{BLUE}re_stock{RESET}/{BLUE}search_shoe{RESET}/{BLUE}value_per_item{RESET}/"
                        f"{BLUE}highest_qty{RESET}/{BLUE}exit{RESET}? ")

    # Capture a shoe oject and add it to the shoe list and inventory file if user_option is equal to 'capture_shoes'
    if user_option == "capture_shoes":
        capture_shoes()

    # Display all the shoe objects in the shoe_list in a table if user_option is equal to 'view_all'
    elif user_option == "view_all":
        view_all()

    # Find and lowest quantitiy of shoe and check if re-stock is needed if user_option is equal to 're_stock'
    elif user_option == "re_stock":
        re_stock()

    # Find and display the shoe detail if shoe object was found if user_option is equal to 'seach_shoe'
    elif user_option == "search_shoe":
        search_shoe()

    # Display the total value of each shoes in shoe_list if user_option is equal to 'value_per_item'
    elif user_option == "value_per_item":
        value_per_item()

    # Find and print out the highest quantitiy of shoe if user_option is equal to 'highest_qty'
    elif user_option == "highest_qty":
        highest_qty()

    # Exit the program if user_option is equal to 'exit'
    elif user_option == "exit":
        print(f"{GREEN}Thank you for using shoe inventory system, bye!{RESET}")
    else:
        print(f"{RED}Oops - incorrect option{RESET}")