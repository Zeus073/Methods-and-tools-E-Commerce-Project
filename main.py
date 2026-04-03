from user import *
from cart import *
from inventory import *
from history import *


## COMPLETE initial pre-login menu
def initialMenu():
    ## objects for the classes
    user = User()
    cart = Cart()
    inventory = Inventory()
    history = OrderHistory()

    ## initial menu
    while(1):
        print("Pre-Login Menu:")
        print("0. Login")
        print("1. Create Account")
        print("2. Exit Program")
        initial = input("Enter your menu choice: ")
        print()

        if(initial == "0"):
            user.login()

        elif(initial == "1"):
            user.createAccount()

        ## exit program
        elif(initial == "2"):
            print("Good-bye!")
            break

        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")

        print()

        ## checks status after one menu loop...
        ## goes into main menu if applicable
        if(user.getLoggedIn()):
            mainMenu(user, cart, inventory, history)


## incomplete main menu...
def mainMenu(user, cart, inventory, history):
    while(user.getLoggedIn()):
        print("Main Menu:")
        print("0. Logout")
        print("1. View Account Information")
        print("2. Inventory Information")
        print("3. Cart Information")
        print("4. Order Information")
        option = input("Enter your menu choice: ")
        print()

        ## logging out
        if(option == "0"):
            user.logout()

            print("Successful logout.")
        
        ## (B) viewing account information. Function already created in user class
        elif(option == "1"):
            user.viewAccountInformation()

        ## (B) Inventory Information
        elif(option == "2"):
            while True:
                print("Inventory Menu:")
                print("0. Go Back")
                print("1. View Inventory")
                print("2. Search Inventory")
                print("3. Decrease Stock")
                choice = input("Enter your choice: ")
                print()

                if(choice == "0"):
                    break
                elif(choice == "1"):
                    inventory.viewInventory()
                elif(choice == "2"):
                    inventory.searchInventory()
                elif(choice == "3"):
                    ## START
                    print("\n-- Decrease Stock --")

                    isbn_input = input("Enter the ISBN of the book to decrease: ")

                    while True:
                        quantity_input = input("Enter the quantity to decrease by: ")
                        try:
                            quantity_to_decrease = int(quantity_input)
                            if quantity_to_decrease > 0:
                                break
                            else:
                                print("Quantity must be positive.")
                        except ValueError:
                            print("Invalid input, Please try again.")

                    inventory.decreaseStock(isbn_input, quantity_to_decrease)
                    
                else:
                    print("Invalid choice. Please try again.")


            

        ## (B) order information
        elif(option == "4"): # (B) submenu for interracting with orders and order history
            while True:
                print("Order Information Menu:")
                print("0. Go Back")
                print("1. View Order History")
                print("2. View Specific Order")
                choice = input("Enter your choice: ")
                print()

                if(choice == "0"):
                    break   # (B) just breaks out of this loop, not fully out of mainMenu()
                elif(choice == "1"):
                    history.viewHistory(user.getUserID()) # (B) calls the viewHistory function from the history class with the userID as argument
                elif(choice == "2"):
                    orderID = input("Enter Order ID: ") # (B) prompt user for specific Order ID
                    #-Unifinished-  history.viewOrder(user.getUserID(), orderID) # (B) calls the viewOrder function from the history class with the userID as argument
                else:
                    print("Invalid choice. Please try again.")
                print()

        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")

        print()


def main():
    print("Welcome to the online bookstore!\n")

    initialMenu()

main()
