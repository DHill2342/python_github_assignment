print("Welcome to my Python program!")
sales = input("How much did we make in sales today? ")
sales = float(sales)
weekly_sales = sales * 7
print("If we make that each day, we'll make $", weekly_sales, "this week.")
try:
    sales = float(sales)
except ValueError:
    print("Please enter a valid number.")
    exit()