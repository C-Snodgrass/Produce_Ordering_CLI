# Chris Snodgrass 113255

def printWelcome():
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
    printWelcome()
    while True:
        try:
            usr_selection = int(input())
            if (usr_selection == 0):
                print("Good Bye")
                break
            elif (usr_selection == 1):
                print("selection")
            elif (usr_selection == 2):
                print("selection")
            else:
                print("Invalid selection...")
        except ValueError:
            print("Invalid selection...")


# caclulate the order value
def calc_order_cost():
    return


# write the order to disk
def write_order():
    return


def buy_products():
    '''
    TODO Read Products and prices form DB
    Display list of produce and prces on the screen with instrucitons for customer order produce
    validate input
    calc price and display order details
    ask for confirmaiton
    yes -> write to disk && aks to quit or return to menu
    no ->  ask to quit or return to menu
    '''


print("in main")
main_menu()
