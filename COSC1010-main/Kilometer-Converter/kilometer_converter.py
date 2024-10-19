#
# christian Espinoza 
# 09/25/2024
# Kilometer Converter Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

    #Void function main
def main():
    #Did some expirimenting, turns out you can put user input as the argument (the piece of data that's passed into a function)
    #A variable returning function, the variable awaits the function to return a new value.
    distanceInMiles = conversionMiles(float(input("Please Enter a Distance In Kilometers: "))) 
    #A print statement that specifies distance with the returned value and rounds to the nearest hundreths.
    print(f"\nYour distance in miles was:{distanceInMiles: .2f} Miles!!!!!")

# A void function to convert the parameter (the user input) into miles. 
def conversionMiles(distanceInKilo):
    #Return function returns a value of an expression, so no need for a local variable just using the given 
    #number for miles.
    return distanceInKilo * 0.6214

#Calls the function, which calls another function!!!!
main()