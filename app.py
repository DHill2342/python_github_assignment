print("Welcome to my Python program!")  #Welcome message
sales = input("How much did we make in sales today? ") #User input for sales
sales = float(sales) #Converts sales input to sales float
weekly_sales = sales * 7 #Calculates the weekly sales based on sales input
print("If we make that each day, we'll make ${weekly_sales} this week.") #Prints weekly sales with supporting text
try:
    sales = float(sales)
except ValueError:
    print("Please enter a valid number.")
    exit() #Exits the program if input is invalid