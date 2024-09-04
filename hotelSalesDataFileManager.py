
# This program allows a hotel salesperson to enter sales into a text file.
# Each line contains the following, separated by semicolons:
# --- name of client
# --- the service sold
# --- amount of the sale
# & displays an error if the amount is not correctly formatted.

# Then the program reads the file and displays
# the total amount for each service category;
# displays an error if the file does not exist.


# -------------------------


# Creates primary function for user to input sales data;
# Writes the data to a text file.
def enterSalesData():
    # Creates empty lists to input multiple sales value entries.  
    customers = []
    services = []
    sales = []
    # Creates strings of valid input characters for currency and names.
    validSales = '1234567890.'
    validNames = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ- '

    #Opens &/or creates the text file for storing the data entered.
    salesFile = open("salesdata.txt", 'a')

    
   # Loop asks for user to input customer name.
    while True:
        customerName = input("Please input the name of the client: ")
        # Catches invalid inputs and re-prompts user to enter name.
        if all(char in validNames for char in customerName):
            break
        print("Error: Invalid Input")

    print(" ")

    # Loop asks user to input selection for service type.        
    print("Please input the service type: ")
    if True:
        serviceType = (input("Enter: \n 1 for Dinner, \n 2 for Conference, \n 3 for Lodging, \n or 4 for Other: "))
        # Prevents invalid inputs and ensures integrity of end totals.
        while serviceType not in ('1','2','3','4'):
            serviceType = (input("\n Error: Please enter: \n 1 for Dinner, \n 2 for Conference, \n 3 for Lodging, \n or 4 for Other: "))

    # Replace selection input numbers with plain text values for final output.
    for i in serviceType:
        if serviceType == '1':
            serviceType = "Dinner"
        if serviceType == '2':
            serviceType = "Conference"
        if serviceType == '3':
            serviceType = "Lodging"
        if serviceType == '4':
            serviceType = "Other"


    print(" ")

    
    # Loop asks user to input the sale amount.
    while True:
        try:
            saleAmount = (input(str("Please input the amount of the sale in numerical format (ex: 29.99): ")))
            # Creates an exception for non-numerical currency value to avoid calculation error:
            if "$" in saleAmount:
                raise ValueError("Error: Sale amount cannot contain currency symbols. ")
            # Catches any invalid/non-number, non-decimal value inputs:
            if all(char in validSales for char in saleAmount):
                break
            print("Error: Invalid Input. ")
            # Prints '$' exception.
        except ValueError as e:
            print(e)
        # raise Exception()


    print(" ")

    # Appends user input values to corresponding lists.        
    customers.append(customerName)
    services.append(serviceType)
    sales.append(saleAmount)
    

    # Writes list data to text file.
    with open("salesdata.txt", "a") as salesFile:
        for i in range(len(customers)):
            line = f"{customers[i]};{services[i]};{sales[i]}\n"
            salesFile.write(line)


    print(" ")

    # Finishes and closes the file.
    salesFile.close()
    print("Data saved successfully to salesdata.txt ")
    print(" ")
    print("------")
    print(" ")


# -------------------------


# Creates supplementary function to re-prompt user to enter into enterSalesData() again
# for further input:
def enterAgain():
    enterAgain = input("Do you want to add another record to the file? Enter 1 for yes or 2 for no. ")
    # Allows user to enter again or continue on to next function and read file.
    while True: 
        if enterAgain == '1': # if yes, enter enterSalesData() again.
            print(" ")
            enterSalesData()
        elif enterAgain == '2': # if no, continue on to readSalesData().
            break
        elif enterAgain != '1' or enterAgain != '2': # if neither/invalid input, re-prompt user to re-enter.
            enterAgain = input("Error: Please enter 1 to add more records or 2 to finish: ")
        else:
            continue
        enterAgain = input("Do you want to add another record to the file? Enter 1 for yes or 2 for no. ")


# -------------------------


# Creates secondary function to read the data entered from
# the previous function, enterSalesData().
def readSalesData():
    # Attempts to open file created by previous function.
    try:
        salesFile = open("salesdata.txt", "r")
    # Creates exception if the file does not exist.
    except FileNotFoundError:
        print("Error: The sales data file does not exist or was not found. ")
        return

    # Initialize variables to store calculated totals.
    totalDinnerSales = 0
    totalConferenceSales = 0
    totalLodgingSales = 0
    totalOtherSales = 0
    totalAllSales = 0
    numOfCustomers = 0

    # Separates values in lists and evaluates them to calculate totals.
    for line in salesFile:
        customerName, serviceType, saleAmount = line.strip().split(";")
        # Converts currency to float for calculation.
        saleAmount = float(saleAmount)
        numOfCustomers += 1
        totalAllSales += saleAmount

        # Calculates the totals from the input categories.
        if serviceType == "Dinner":
            totalDinnerSales += saleAmount
        if serviceType == "Conference":
            totalConferenceSales += saleAmount
        if serviceType == "Lodging":
            totalLodgingSales += saleAmount
        if serviceType == "Other":
            totalOtherSales += saleAmount

    # Closes the file after completion.
    salesFile.close()
    

    # Prints calculated results to the user.                
    print(f"Total number of customers: {numOfCustomers}")
    print(f"Total dinner sales: ${totalDinnerSales: .2f}")
    print(f"Total conference sales: ${totalConferenceSales: .2f}")
    print(f"Total lodging sales: ${totalLodgingSales: .2f}")
    print(f"Total other sales: ${totalOtherSales: .2f}")
    print(" ")
    print(f"Total sales: ${totalAllSales: .2f}")


# ---------------------


# Calls functions in operating order:

enterSalesData()

enterAgain()


print(" ")

readSalesData()
    
