#
# Christian Espinoza 
# 10/22/2024
# Average of Numbers Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 


def main():
    #Variable referencing the file object. While opens the file.
    theNumbersGiven = open(r'numbers.txt', 'r')

    average = 0 #Declares the average variable.

    theTotalForNumbers = 0 # Declares the variable for the total.

    totalLines = 0 #Declares the variable that counts the lines.

    for theAmountOfLines in theNumbersGiven: #Starts the loop to check each line iteration.

        print(theAmountOfLines) #Print the line in the numbers file.

        changingData = float(theAmountOfLines) #Change the data from a string to a float. 

        theTotalForNumbers += changingData #Add the newly cconverted number to the total.
        totalLines += 1 #Add one to the total amount of lines checked.
    theNumbersGiven.close()
    average = theTotalForNumbers/totalLines #Finally, take the total variable and divide that with the amount of lines.
    print('The average of the Numbers is: ',  average) #Print the results. 

    try: 
        main()
    except IOError:
        print("The File is not connected to the program")
    except ValueError:
        print("Invalid output is present in the file. A line contains not a number. ")
    
main()