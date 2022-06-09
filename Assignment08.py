# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Johnathan Luu,6.6.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Johnathan Luu,6.6.2022,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to the Product class
    def __init__(self, product_name, product_price):

        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("An error has occured setting initial values: "+ str(e))

    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("The product name cannot be numeric")

    @property
    def product_price(self):
        return float(self.__product_price)
    
    @product_price.setter
    def product_price(self, value):
        if str(value).isnumeric():
            self.__product_price = value
        else:
            raise Exception("The price must be a number")


    def __str__(self):
        return self.product_name + "," + str(self.product_price)

        

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Johnathan Luu,6.6.2022,Modified code to complete assignment 8
    """
    pass

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        success_status = False
        try:
            file = open(file_name, "w")
            for product in list_of_product_objects:
                file.write(product.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was an error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):

        lstProducts = []
        
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                lstProducts.append(row)
            file.close()
        except Exception as e:
            print("There was an error")
            print(e,e.__doc__, type(e), sep='\n')
        return lstProducts

# Processing  ------------------------------------------------------------- #



# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    '''A class to carry out a main menu and provide options
    
    methods:
        DisplayMenu():
        
        MenuChoice():
        
        CurrentData():
        
        AddData():
        '''
    pass


    # TODO: Add code to show menu to user
    @staticmethod
    def DisplayMenu():
        """  Display a menu of choices to the user
        """
        print('''
        Menu of Options
        1) Show current products
        2) Add a new item
        3) Save Data to File        
        4) Exit Program
        ''')
        print()


    # TODO: Add code to get user's choice
    @staticmethod
    def MenuChoice():
        option = str(input("Choose an option (1-4) ")).strip()
        print()
        return option


    # TODO: Add code to show the current data from the file to user
    def CurrentData(RowLst):
        print("The current products are: ")
        for row in RowLst:
            print(row.product_name + ", " + str(row.product_price))
            print()

    # TODO: Add code to get product data from user
    def AddData():
        try:
            item = ''
            product = str(input("Enter a product name: ").strip())
            price = float(input("Enter its price: ").strip())
            item = Product(product_name = product, product_price = price)
        except Exception as e:
            print(e)
        return item
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
try:
    lstofProducts = FileProcessor.read_data_from_file(strFileName)

    while True:
        # Show user a menu of options  
        IO.DisplayMenu()
        # Get user's menu option choice
        Choice = IO.MenuChoice()
        if Choice.strip() == '1':
            # Show user current data in the list of product objects
            IO.CurrentData(lstofProducts)
            continue
        elif Choice.strip()=='2':
            # Let user add data to the list of product objects
            lstofProducts.append(IO.AddData())
            continue
        elif Choice.strip() == '3':
            # let user save current data to file and exit program
            FileProcessor.save_data_to_file(strFileName, lstofProducts)
            continue
        elif Choice.strip() =='4':
            break
except Exception as e:
    print("There was an error: ")
    print(e,e.__doc__, type(e), sep = '\n')

        

# Main Body of Script  ---------------------------------------------------- #

