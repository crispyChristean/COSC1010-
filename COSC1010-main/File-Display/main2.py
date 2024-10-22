#
# Christian Espinoza Celis
# 10/22/2024
# File Display Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program (Not this time)

    #Opens the numbers.txt file and sets it to read only mode.
    #The r prefix references that this is a raw string we are referencing for the file.
numbersObject = open(r'numbers.txt', 'r') #Create the variable that references the file object

# In this statement we are setting the for loop to the local variable IN the file object (the variable)

#readingTheNumbers shows the current iteration in the object. 
for readingTheNumbers in numbersObject: #For loops automatically iterate through each line of the file.
    print(readingTheNumbers) #Print out the iteration in the text file.
numbersObject.close() #Closes the file.