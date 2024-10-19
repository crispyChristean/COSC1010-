#
# Christian Espinoza Celis
# 10/18/2024
# File Display Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 


def main(): # Creates the main function that declares the start of the program.

    usingAWhileLoop() #Declares the function.


def readingAllContent(): #Creates a function that reads and prints with a for loop. 
    #Opens the numbers.txt file and sets it to read only mode.
    #The r prefix references that this is a raw string we are referencing for the file.
    numbersObject = open(r'numbers.txt', 'r') #Create the variable that references the file object

# In this statement we are setting the for loop to the local variable IN the file object (the variable)
#During the loop is executed. 

# If I had to decribe what is going on is we are setting the variable and the file content that is opened, 
# will have the loop go through each line as a value until there is no value.
# In each value (line) the variable readingTheNumbers will be set to that line. (from observation). 


    for readingTheNumbers in numbersObject: #For loops automatically iterate through each line of the file.
        print(readingTheNumbers) #In each interation it will print what value it is currently assigned to. 
    numbersObject.close() #Once the loop is exited, it will close the file.

#This function is testing how to write all the contents but with a while loop instead. Ignorable program. 
def usingAWhileLoop(): # Creates a function that reads and prints the txt file but with a while loop.
    numbersObjectTwo = open(r'numbers.txt', 'r')

    referenceVariable = numbersObjectTwo.readline()

    while referenceVariable != '':
        print(referenceVariable)
        referenceVariable = numbersObjectTwo.readline()
    numbersObjectTwo.close()

# WHERE THE ACTUAL START PROGRAM EXIST
main()

# While I understand what I am doing I am slightly confused as to how is there spacing being produced without a \n statement.