import sqlite3
import sys
import random
'''
 OrderHistory
 - databaseName: string

 + OrderHistory()
 + OrderHistory(string databaseName)
 + viewHistory(string userID): void
 + viewOrder(string userID, string orderID): void
 + createOrder(string userID, int quantity, float cost,
 string date): string
 + addOrderItems(string userID, string orderID): void
'''
class OrderHistory:

    def __init__(self, databaseName="methods.db"):
        self.databaseName = "methods.db"


    def viewHistory(self, userID):
        
        ## (B) attempt to connect to the database
        try:
            connection = sqlite3.connect(self.databaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()

        ## (B) basis taken straight from user.py code with some adaptations
        ## cursor to send queries through
        cursor = connection.cursor()

        ## sets up query and uses user input for the constraint
        ## selects specific information to return based on the userID
        query = "SELECT OrderNumber, ItemNumber, Cost, Date FROM Orders WHERE UserID = ? ORDER BY Date DESC" # (B) changed to be in descending order by date
        data = (userID,) # (B) prevents SQL injection, userID is what we are using to find the correct orders to return

        cursor.execute(query, data)
        result = cursor.fetchall()

        ## nothing was grabbed
        if(len(result) == 0):
            print("\nInformation is not in the system.")
        else:
            print("Your past orders:")
            for OrderNumber, ItemNumber, Cost, Date in result:
                print(f"- Order #{OrderNumber} | Cost: {Cost} | Items: {ItemNumber} | Date: {Date}")

        ## closes connection
        cursor.close()
        connection.close()