#
# Christian Espinoza    
# 9/22/2024
# Bug Collector Programming Project
# COSC 2409 DNT

# Initialize variables for bugs and total number of bugs collected.
numberOfBugs = 0
totalBugs = 0 
numberOfDays = 0 

# Get number of bugs collected each day using a for loop.
while (numberOfDays !=5):
#While loops basically combine boolean statements into a for loop in my opinion. 
    numberOfBugs = int(input("How many bugs did you collect today? "))
# User input, ask for the number.
    totalBugs = totalBugs + numberOfBugs 
# takes that number and adds to the total.
    numberOfDays = numberOfDays + 1
#Takes a variable to count the days and adds one. Ensures it stops at 5 days.

# Display the total number of bugs collected.

print(f"The Number of Bugs you collected within a period of 5 days is: {totalBugs}")
