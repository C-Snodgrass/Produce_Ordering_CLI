# Chris Snodgrass 113255
import sqlite3
import sql
import admin


def print_welcome():
    print("***********************************************")
    print("*          Welcome to the Stardew Valley      *")
    print("*            Online Store & Emporium          *")
    print("*                                             *")
    print("*          Explore Our Bountiful Selection    *")
    print("*            of Seeds, Tools, and More!       *")
    print("*                                             *")
    print("*        Step Into a World of Farming Magic   *")
    print("*                                             *")
    print("*        Please select from the following     *")
    print("*                 options below:              *")
    print("*                                             *")
    print("*      1. Buy Products                        *")
    print("*      2. Admin Login                         *")
    print("*      0. Quit                                *")
    print("***********************************************")


def main_menu():
    print_welcome()
    while True:
        try:
            usr_selection = int(input())
            if (usr_selection == 0):
                print("Good Bye")
                break
            elif (usr_selection == 1):
                buy_products()
            elif (usr_selection == 2):
                admin.admin_login()
            else:
                print("Invalid selection...")
        except ValueError:
            print("Invalid selection...")


# caclulate the order value
def check_out(order):
    order = {"Item": ,
             "Variety": ,
             }
    sql.create_new_order(order)
     
    return


# write the order to disk
def write_order():
    return




'''
    TODO Read Products and prices form DB
    calc price and display order details
    ask for confirmaiton
    yes -> write to disk && aks to quit or return to menu
    no ->  ask to quit or return to menu
    '''


def buy_products():
    connection = sqlite3.connect('produce.db')
    cursor = connection.cursor()
    # Pass SQL SELECT statement into .execute() method of the cursor object
    cursor.execute("SELECT * FROM produce;")
    # Use .fetchall() method of the cursor object to fetch the data
    produce = cursor.fetchall()
    print("{:<5} {:<10} {:<20} {:<10} {:<10}".format("ID", "Type", "Variety", "Available", "Price"))
    for product in produce:
        print("{:<5} {:<10} {:<20} {:<10} ${:.2f}".format(*product))

    connection.close()
    num_of_items = len(produce)
    
    order = []
    while True:
        try:
            choice = int(input("To purchase some produce, please select the product id from the list. or 0 to check out"))
            if (choice == 0):
                check_out(order)
            elif (choice < 0 or choice > len(produce) - 1):
                print("Invalid selection...")
            else:
                quantity = int(input("Plese input quantity in KG: "))
                new_order = (choice - 1, quantity)
                order.append(new_order)
                print("select another or 0 to check out")
                
        except ValueError:
            print("Invalid selection...")




print("main")
# sql.create_tables_if_not_exist()
# sql.insert_synthetic_produce()
main_menu()
