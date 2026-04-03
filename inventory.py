import sqlite3
import sys

class Inventory:

    ## Constructor
    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName  # store the database name

    ## Function to view the inventory
    def viewInventory(self):
        
        try:
            connection = sqlite3.connect(self.databaseName)
            
        except:
            print("Failed database connection.")
            sys.exit()

        cursor = connection.cursor()

        query = "SELECT ISBN, Title, Author, Genre, Pages, ReleaseDate, Price, Stock FROM Inventory ORDER BY Title ASC"

        cursor.execute(query)
        result = cursor.fetchall()

        if len(result) == 0:
            print("No Inventory Found.")
        else:
            print("Current Inventory:\n")
            for ISBN, Title, Author, Genre, Pages, ReleaseDate, Price, Stock in result:
                print(f"{Title} by {Author}")
                print(f"    ISBN: {ISBN}")
                print(f"    Genre: {Genre}")
                print(f"    Pages: {Pages}")
                print(f"    Release Year: {ReleaseDate}")
                print(f"    Price: ${Price}")
                print(f"    In Stock: {Stock}\n")

        ## closes connection
        cursor.close()
        connection.close()

    
    def searchInventory(self):
        
        
        try:
            connection = sqlite3.connect(self.databaseName)
            
        except:
            print("Failed database connection.")
            sys.exit()
        
        cursor = connection.cursor()

        ## Begin to ask for search options for user
        print("\nSearch Options:")
        print("1. Title")
        print("2. Author")
        print("3. ISBN")
        print("4. Genre")

        while True:
            choice = input("Enter the number in which you wanna search by (1-4): ")
            if choice == '1':
                search_field = "Title"
                break
            elif choice == '2':
                search_field = "Author"
                break
            elif choice == '3':
                search_field = "ISBN"
                break
            elif choice == '4':
                search_field = "Genre"
                break
            else:
                print("Invalid Choice, please enter a number between 1 to 4.")
                

        search_term = input(f"Enter the search term for {search_field}: ")

        
        query = f"SELECT ISBN, Title, Author, Genre, Pages, ReleaseDate, Price, Stock FROM Inventory WHERE {search_field} LIKE ? ORDER BY Title ASC"
        
       
        search_parameter = ('%' + search_term + '%',)

        
        cursor.execute(query, search_parameter)
        result = cursor.fetchall()

        ## Display Results below
        if len(result) == 0:
            print(f"\nNo Inventory Items found that match '{search_term}' in {search_field}")
        else:
            print(f"\n--- Search Results for {search_field}: '{search_term}' ---")
            for ISBN, Title, Author, Genre, Pages, ReleaseDate, Price, Stock in result:
                print(f"{Title} by {Author}")
                print(f"    ISBN: {ISBN}")
                print(f"    Genre: {Genre}")
                print(f"    Pages: {Pages}")
                print(f"    Release Year: {ReleaseDate}")
                print(f"    Price: ${Price}")
                print(f"    In Stock: {Stock}\n")

        ## closes connection
        cursor.close()
        connection.close()

    def decreaseStock(self, ISBN, quantity=1): 
            try:
                connection = sqlite3.connect(self.databaseName)
                
            except:
                print("Failed database connection.")
                sys.exit()
            
            cursor = connection.cursor()
            
            ## Error check for negative values
            if not isinstance(quantity, int) or quantity < 0:
                print(f"Error: Quantity must be a positive integer.")
                cursor.close()
                connection.close()
                return
            

            check_query = "SELECT Stock, Title FROM Inventory WHERE ISBN = ?"

            cursor.execute(check_query, (ISBN,)) 
            result = cursor.fetchone()

            if result is None:

                print(f"Error: Book with ISBN '{ISBN}' not found in inventory.")
            else:
                current_stock, title = result[0], result[1]

                new = current_stock - quantity
                
                ## Decrease the stock
                if new < 0:
                    print(f"Error: Cannot decrease stock.")
                else:

                    update_query = "UPDATE Inventory SET Stock = ? WHERE ISBN = ?"

                    cursor.execute(update_query, (new, ISBN))
                    connection.commit()
                    print(f"Successfully decreased stock.")

            cursor.close()
            connection.close()

