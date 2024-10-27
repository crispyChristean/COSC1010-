#
# Christian 
# 10/23/2024
# Magic 8 Ball Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
import random 

def main():
    wordSequence = [] #Declares an array.

    ballResponse = open(r'8_ball_responses.txt', 'r') #Opens the file and sets it in read mode.

    checking = '' #Sets an emtpy String.
#Decalares a for loop that takes a variable and reads the line of the txt file, while doing so it attaches each line to a value in an array.
    for number in ballResponse: 
        wordSequence.append(number)
#Once the program reaches the end of the file it then closes the file as it's no longer needed.
    ballResponse.close()
#We will then attach the checking variable to an input that ask to enter a prompt.
#Sets a while condition that while checking is a string:
    while checking !="EXIT":
        checking = input("Please Enter a prompt for the 8 ball to Ask\n (If you would like to exit the program enter EXIT): ")
        if checking == "EXIT":
            break
        #It gets a random number from the range of the number given from the length of the array.
        chosen = wordSequence[random.randrange(len(wordSequence))] #This essentially determines what index is called by a serious of methods that get the length and then produce a random value from that range.
        print("THE 8 BALL SPEAKS, IT SAYS: ", chosen) #It will then print out the chosen value from the chosen random index.
        checking = input("Would you like to ask another question? If not enter 'EXIT'") #It will then ask the user if it wants to ask another question or to exit.
    return #Once the SENTINEL is entered, it will then exit out of the main function, thus ending the program. 


main()