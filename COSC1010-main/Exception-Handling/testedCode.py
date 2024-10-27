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
    


    #Experimented Code that resulted in a recursion error. This is because we are trying the function within the function.
    #try: 
        #main()
    #except IOError:
        #print("The File is not connected to the program")
        #exit()
    #except ValueError:
        #print("Invalid output is present in the file. A line contains not a number. ")
        #exit()


try: 
    main()
except IOError:
    print("The File is not connected to the program")
    exit()
except ValueError:
    print("Invalid output is present in the file. A line contains not a number. ")
    exit()
