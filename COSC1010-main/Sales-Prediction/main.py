#
# Christian
# 09/07/2024
# Sales Prediction Programming Project
# COSC 2409 DNT
#




# Variables to hold the sales total and the profit

profitPercentage = .23

# profitPercentage variable is being assigned here.
# The value is .23 and the variable stores it as a float data type.

# Get the amount of projected sales.

projectedSales = float(input("What is the Projected amount of total sales? "))
# The input function is being declared here, but when we do enter input, 
# it'll store it as a string, which is why we have to re-assign it,
# by putting the float function outside the input function.

# Calculate the projected profit.

projectedProfit = projectedSales * profitPercentage

# A variable that performs an operation between projectedSales (which the number varies) and profitPercentage (.23)
# Print the projected profit.

print(f"The projected profit from the total: ${projectedProfit:.2f}")

# The print statement prints text and then passes the argument to the variable that displays its value.

# EDIT: After reviewing the textbook I decided to change the code to a f-string and use a format specifier 
# (the type that rounds floating poinnt numbers) to better 
# show that this is money we are dealing with.