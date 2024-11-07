#
# Christian Espinoza 
# 11/6/2024
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 


def main():
    #Gets input from the user. 
    getTheSentence = input("Please Enter a Sentence to convert to Pig Latin: \n")
    #Takes the input as an argument. 
    convertToPig(getTheSentence)

#Starts the function for conversion.
def convertToPig(given):
    #Gets a new variable that is an array that includes each word. 
    newSentence = given.split()
    #Creates a variable to be used later. 
    conversion = []
    #Creates a string to be used later. 
    organizing = ""

    #print(newSentence) this code can check the array that includes the user input. Each word included. 

#When using a loop in an array that contain strings, you can also reference the index of that string as well. An index within an index!!!

#For each string in the array NewSentence: (the loop will repeat until hitting the last word)
    for iteration in newSentence:
        #It'll first check if the word is less than 1 in terms of length (index), if so...
        if len(iteration) <= 1:
            #Add the current iteration word into the conversion array. 
            conversion.append(iteration)
            #add the "ay" to the conversion array. 
            conversion.append('ay')
            #Then for each item in the conversion array..
            for eachWord in conversion:
                #add the current element/value at the iteration the array is at to the string (convert the value to a string).
                organizing += str(eachWord)
            #After adding the word, add a space to indicate a new word is beginning in the organizing string. 
            organizing += " "
            #emtpy the conversion array.
            conversion = []
        #print(iteration[0])
        #print(iteration[1])
        else:
            #If the current word is bigger than 1, append all the contents of the word starting from its index of 1.
            conversion.append(iteration[1:len(iteration)])
            #Then add the first letter of the word after adding all of the other letters. Within the array.
            conversion.append(iteration[0])
            #Add the Ay at the end of the array. 
            conversion.append('ay')
            #For each item in the conversion array.
            for eachWord in conversion:
                #convert the item into a string and add that to the organizing string. 
                organizing += str(eachWord)
            #After all the content is added add a space and emtpy the conversion array.
            organizing += " "
            conversion = []
    print(organizing)

main()

#IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY