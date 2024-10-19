#
# Christian Espinoza 
# 10/18/2024
# Average of Numbers Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 


def main():

    averageOfNumbers()



def averageOfNumbers():

    #Variable referencing the file object. While opens the file.
    theNumbersGiven = open(r'numbers.txt', 'r')

    average = 0 

    theTotalForNumbers = 0

    totalLines = 0

    for theAmountOfLines in theNumbersGiven:

        print(theAmountOfLines)

        changingData = float(theAmountOfLines)

        theTotalForNumbers += changingData 
        totalLines += 1
    theNumbersGiven.close()
    average = theTotalForNumbers/totalLines
    print('The average of the Numbers is: ',  average)


main()