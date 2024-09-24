# Chrsitian Espinzoa
# 09/22/24
# Budget Analysis Programming Project
# COSC 2409 DNT
# Use comments liberally throughout the program. 

#Sets the budget for the month.
budget = 0 
#Keeps the total amount spent in the program.
totalSpent = 0 
#Stores specified text.
budgetCheck = "0"
#Stores the user input.
expenseItem = 0 

#Ask the user for the budget, sets the budget for the month.
budget = float(input("Please Enter the Budget for this month: "))
#While Loop sets a parameter that as long as the expenseItem(user input) is not a string to continue a task.
while (expenseItem != "break"):
    expenseItem = input("What was the cost of the purchase within this month? (Enter 'break' to finalize the expense for the month)")
    #Test to see if the user puts in break, if so it will exit the loop and execute the output.
    if expenseItem == "break":
        break
    else: 
        #Converts the variable into a float.
        expenseItem = float(expenseItem)
        #Then adds the input into the total
        totalSpent = totalSpent + expenseItem

#Test to see if the printed text should specify if the user was over or under budget.
if totalSpent > budget:
    budgetCheck = "OVER"

elif totalSpent < budget:
    budgetCheck = "UNDER"

else: 
    budgetCheck = "JUST ON THE"
#Print the output, rounds to 2 places.
print(f"Your amount of money you spent for the month was: ${(totalSpent): .2f}.\n \
      Your amount spent was {budgetCheck} budget")