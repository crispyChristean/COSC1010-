#
# Christian
# 09/14/2024
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT

attendanceCookout = 0 
# Declares the variable that will  store the amount of people attending
hotDogPerPerson = 0 
# Declares the variable used that will store how many hotdogs each person has.
amountTotal = 0
# Delcares a variable that will be used to calculate the number of dogs needed (yum)
packsOfDogs = 0
# Declares a variable that will be used to calculate the number of packages of dogs needed.
packsOfBuns = 0 
# Declares a variable to store the amount of packages of buns needed
roundedPackDogs = 0
roundedPackBuns = 0
# Variables that store the actual amount of packages we need (since we can't buy real numbers of packages)
dogComparison = 0
bunComparison = 0
# Variable that will store the two package variables to test whether the package number is not a whole number.
HOT_DOGS = 10 
# Hot dogs come in packages of 10. Here I'm declaring them as constants.
HOT_DOG_BUNS = 8
# Hot dog buns come in packages of 8. Also declaring as a constant.

attendanceCookout = int(input("What is the number of people attending the cookout? "))
#Ask for the number of people attending the cookout 

hotDogPerPerson = int(input("What is the amount of hot dogs given to each person? "))
#ask the number of hot dogs each person will be given

amountTotal = hotDogPerPerson * attendanceCookout
# Gets the total number of hot dogs for the cookout 

packsOfDogs = amountTotal/HOT_DOGS
# Gets the total amount of hot dogs packages needed. 
roundedPackDogs = round(packsOfDogs, 0)
# Rounds the number of hot dog packages
dogComparison = packsOfDogs - roundedPackDogs
# Inserts a value that takes the original number of packages to the rounded.
if dogComparison < 1 and dogComparison > 0:
    roundedPackDogs = roundedPackDogs + 1
#checks to see if the value of dogComparison is a real number, if so adds one to the rounded hot dog packs
#to better represent a number

packsOfBuns = amountTotal/HOT_DOG_BUNS
roundedPackBuns = round(packsOfBuns, 0)
bunComparison = packsOfBuns - roundedPackBuns
if bunComparison < 1 and bunComparison > 0:
    roundedPackBuns = roundedPackBuns + 1
#Same coding with the dogs but instead with the buns.

print("The minimum number of Hot dog Packages needed are:", roundedPackDogs)
print("The minimum number of Hot dog bub Packages needed are:", roundedPackBuns)
#Prints the number recieved from the former code.

dogsLeft = (roundedPackDogs * HOT_DOGS) - amountTotal
bunsLeft = (roundedPackBuns * HOT_DOG_BUNS) - amountTotal

#Gets the value of dogs and buns left by subtracting TOTAL supply from just the amount of hot dogs/buns used.

if dogsLeft == 0 and bunsLeft == 0:
    print("WOW, there are no leftovers!!! :D")
else: 
    print(f"The amount of hot dogs left are: {dogsLeft}")
    print(f"The amount of buns left are: {bunsLeft}")

    # A small decision structure to determine whether neat lil text if printed to show no leftover or to show leftovers.