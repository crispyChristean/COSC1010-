#HEADS UP: THIS IS WHAT I ACTUALLY AM SUBMITTING. THe other python file was experimenting (as in discord)
# Christian Espinoza 
# 10/22/2024
# Average of Numbers Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

def main():

    #We first try to open the desired text file.
    #Variable referencing the file object. While opens the file.
    try:
        theNumbersGiven = open(r'numbers.txt', 'r')
    except IOError:
        #We print out what had happened.
        print("The File is not connected to the program")
        #we then return back into the program outside of the function.
        return 
    average = 0 #Declare the average variable.

    theTotalForNumbers = 0 #Declare the accumulator/total.

    totalLines = 0 #Another accumulator that adds up all the lines.

    for theAmountOfLines in theNumbersGiven: #A variable that goes through each iteration.

        print(theAmountOfLines) #Prints the supposed number.

        #Another try statement that checks if the conversion produces an error.
        try:           
            changingData = float(theAmountOfLines)
        #If the exception does occur we print out a warning.
        except ValueError:  
            print("The value in the line is NOT A NUMBER")
            return
        
        theTotalForNumbers += changingData #Add the converted number to the total.
        totalLines += 1 #Add 1 as we are checking a new line.

    theNumbersGiven.close() #Closes the file.
    average = theTotalForNumbers/totalLines #Gets the average.
    print('The average of the Numbers is: ',  average) #Prints the average.


main()
# I had a misunderstanding of the try except statement. Statements in the try clause are actually executed. 
# Another misunderstanding is that the exceptions are actual error codes and we insert an exception's name
#in the except clause if we encounter such exception as described. 