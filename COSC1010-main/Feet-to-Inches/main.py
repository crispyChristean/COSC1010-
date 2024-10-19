#
# Christian CC
# 09/25/2024
# Feet to Inches Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program.

# Declares the global Constant (in theory)
ONE_FOOT = 12

#Since this one is almost exactly identitical I tried to make it slightly different by adding a while loop
#To keep the program running 


#Void Main Function
def main():
    #variable-returning function that ask for the user input for the argument before passing it to the function.
    converted_to_inches = feet_to_inches(int(input("Please enter your number of feet: ")))

    #Once the value is returned to the variable we use a print statement.
    print(f"The number of inches in that number of feet is: {converted_to_inches} inches")

    #Initiates the loop, ask the user if they would like to run the program again.
    run_again = input("\nWould you like to run the program again?\nEnter 'y' for yes and 'n' for no: ")

    #While loop that serves the condition that'll keep running until the string is "n"
    while run_again != "n":
        #repeats the whole code again until "n" is used.
        converted_to_inches = feet_to_inches(int(input("\nPlease enter your number of feet: ")))
        print(f"The number of inches in that number of feet is: {converted_to_inches}")
        run_again = input("\nWould you like to run the program again?\nEnter 'y' for yes and 'n' for no: ")

def feet_to_inches(numberOfFeet):
    return numberOfFeet * ONE_FOOT

#Calls the function
main()

#I also checked the video and the guy essentialy did the same thing, I understand if I get down graded for adding the loop.