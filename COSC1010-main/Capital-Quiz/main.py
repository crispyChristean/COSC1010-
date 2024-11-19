#
# Christian Espinoza 
# 11/17/2024
# Capital Quiz Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

import random

def main():
    # Initialize dictionary
    capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South       Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

    #Initialize Variables to hold state names, correct/wrong tries, and the sentinel. 
    guessingValue = ""

    numberOfTriesRight = 0 

    numberOfTriesWrong = 0

    SENTINEL = "quit" 
    
    onlyStates = []

    #Add the keys of the capitals dictionary to a seperate tuples.
    for iteration in capitals.keys():
        onlyStates.append(iteration) 

    #start the while condition to begin the game.
    while guessingValue.lower() != SENTINEL:
#Assigns a random state in the tuple.
        randomState = onlyStates[random.randrange(len(onlyStates))]
#Creates an input statement to guess the capital, the input it changed to a lower characters after.
        guessingValue = input(f"(If you wish to exit the program, please enter 'quit') \nGuess the Capital of: {randomState}: ").lower()
#Starts the checking function, passing all the needed local variables.
#Updates the variables from assigning them the variables of the checking function.
        guessingValue, numberOfTriesRight, numberOfTriesWrong = checking(guessingValue, numberOfTriesRight, numberOfTriesWrong, capitals)
#Once the user quits it then produces an output of accumulated attempts right/wrong and thanks the player.
    print(f"The Number of Correct Answers: {numberOfTriesRight} \nThe number of Incorrect Answers: {numberOfTriesWrong} \nThank you For Playing!")


def checking(guessingValue, numberOfTriesRight, numberOfTriesWrong, capitals):
    #Local variable to check if there was a matching value. Set to 0.
    checkingIf = 0
    #Goes through each value in the dictionary. Excludes the keys since we are not matching keys.
    for iteration in capitals.values():
    #If there is a mathcing value, we add one to the local variable.
        if guessingValue.lower() == iteration.lower():
            checkingIf+=1
    #Once the loop ends we check the value of the local variable. If it's larger than one it means there was a match within the dictionary and the answer is correct. 
    #We reset the local variable for the next loop and return the variables back to the main function. 
    if checkingIf == 1:
        print("Correct!")
        numberOfTriesRight+=1
        checkingIf-=1
        return guessingValue, numberOfTriesRight, numberOfTriesWrong
    else:
    #Essentially the same path without the need of resetting the local variable.
        print("Incorrect")
        numberOfTriesWrong+=1
        return guessingValue, numberOfTriesRight, numberOfTriesWrong

            

main()
