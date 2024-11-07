#
# Christian Espinoza
# 11/6/2024
# Vowels and Consonants Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

#function to check Vowels.
def checkingForVowels(givenVariable):
    #Create an accumulator.
    accumulateVowels = 0 
    #Create an array that contains each vowel. Both capital and lowercase.
    allTheVowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    #For each iteration of the Vowels Array:
    for iteration in allTheVowels:
        #Enter another loop that then goes through each iteration of the given word
        for iterationForGiven in givenVariable:
            #If the current iterated letter in the given input matches with the current iteration of the array, add to the accumulator.
            if iteration == iterationForGiven:
                accumulateVowels+=1
    #Once the array's contents have been fully iterated it will then print the amount. 
    print(f'\nThe amount of vowels in the {givenVariable} is: {accumulateVowels}')

#Function to check Consonants, essentially does the same thing as the Vowels functions but checks for consonants.
def checkingForConsonants(givenVariable):
    allTheConstonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S","T", "V", "W", "X", "Y", "Z",\
                        "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    accumulateConstonants = 0

    for iteration in allTheConstonants:
       
        for iterationForGiven in givenVariable:

            if iteration == iterationForGiven:
                accumulateConstonants+=1
                
    print(f'\nThe amount of Constonants in the {givenVariable} is: {accumulateConstonants}')
   
def main():
    #Gets the word for the user.
    theGivenString = input("Please enter a string to check for Vowels and Consonants: ")
    #Executes the two function with the word as the argument that's passed. 
    checkingForVowels(theGivenString)
    checkingForConsonants(theGivenString)
    
#Function to check for vowels. 

main()