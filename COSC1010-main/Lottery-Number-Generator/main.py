#
# Christian Espinoza
# 10/22/2024
# Lottery Number Generator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

#imports the random module.
import random

def main(): 
    checkForRepeat = 0 # A variable to check repeated seeds.
    generatedNumber = 0 # A variable to associat the random number.
    organizedNumber = "" # A variable make the lotto ticket number.

    #Declares an empty list sequence.
    lottoNumber = []


    for counter in range(0,7):
        #Generates number
        generatedNumber = random.randrange(0, 10)
        #If statement checks if the generated number repeats the last, if so generate one more time.
        if random.seed() == checkForRepeat:
            generatedNumber = random.range(0,10)
        #Add that generated number to the array.
        #You can add a print statement here to check what my code is doing. 
        lottoNumber.append(generatedNumber)
        #associate the current number to the variable for comparison in the next loop.
        checkForRepeat = generatedNumber

    print("\n")

    #starting at the beginning of the index, newLength will equal to that index iteration. While so:
    for newLength in lottoNumber:
        organizedNumber += str(newLength) #Convert the number into a string and add that string to the variable.


    print(f"Your Lotto Number is: {organizedNumber}!!!")

    print(f"\nWe could also leave it in the sequence format: {lottoNumber}")

    #The bottom produced an error, this is because you're referencing the value in that current index ideration.
    #Which when trying to then use that variable to call the index in our sequence, could and will be out of that sequence. Such as 10 or 9 when the index only goes up to 8.
    #There is also no reason to call the index again as the already associated for variable does so. 

        #organizedNumber += str(lottoNumber[newLength]) 

main()