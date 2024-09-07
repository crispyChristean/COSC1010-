#
# Christian
# 09/07/2024
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations

# Constants for the state and county tax rates
STATE = .025

COUNTYTAX = .05

# Get the amount of the purchase.
purchaseAmount = float(input("Enter the amount of the purchase: "))
#Converting the input from a string to a float. As we are dealing with money.
# Calculate the state sales tax.
state_tax_total = STATE * purchaseAmount
# Calculate the county sales tax.
county_tax_total = COUNTYTAX * purchaseAmount
# Calculate the total tax.
total_tax = state_tax_total + county_tax_total
# Calculate the total of the sale.
totalSale = (purchaseAmount + total_tax)
# Print information about the sale.

# No worries of converting or dealing with data types as they all carry the same data of "float"
print(f"The amount of the purchase: {purchaseAmount:.2f}\nState Sales Tax: {state_tax_total:.2f}\n County Sales Tax: {county_tax_total:.2f}\nThe total sales tax: {total_tax:.2f}\n The total of the Sale: {totalSale:.2f}")