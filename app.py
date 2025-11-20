print("Welcome to my Python program!")  #Welcome message
sales = input("How much did we make in sales today? ") #User input for sales
try:
    sales = float(sales) #Converts input to float (anticipated type)
except ValueError:
    print("Please enter a valid number.") #Error message for invalid input
    exit() #Exits the program if input is invalid
weekly_sales = sales * 7 #Calculates the weekly sales based on sales input
print(f"If we make that each day, we'll make ${weekly_sales: .2f} this week.") #Prints weekly sales with supporting text