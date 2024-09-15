# Instructions  

Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. The program should ask the user for the number of people attending the cookout and the number of hot dogs each person will be given. The program should display the following details:

- The minimum number of packages of hot dogs required
- The minimum number of packages of hot dog buns required
- The number of hot dogs that will be left over
- The number of hot dog buns that will be left over




***NOTE: IGNORE, this was code that I was experimenting with before coming to my final conclusion as to my approach***
if amountTotal < 10: 
    print(f'The number of hot dog packages needed are: 1')
    print(f'The number of Hot Dog Bun Packages needed are: 1')

elif amountOfPackages <= 1 or amountOfBunPackages <= 1:
    print(f'The number of hot dog Packages = 1')
    print(f"The Number of Packages needed for the Hot Dog Buns are: 1")











    if amountOfPackages == float(amountOfPackages):
    roundedPackages = round(amountOfPackages, 0)
    print(f"The number of hot dog packages neede are: {roundedPackages}")
    print(f"The Number of Packages needed for the Hot Dog Buns are: {amountOfBunPackages}")

elif amountOfBunPackages == float(amountOfBunPackages):
    roundedBuns = round(amountOfBunPackages, 0)
    print(f"The number of hot dog packages needed are: {amountOfPackages}")
    print(f"The Number of Packages needed for the Hot Dog Buns are: {roundedBuns}")

elif amountOfBunPackages == float(amountOfBunPackages) and amountOfPackages == float(amountOfPackages):
    roundedPackages = round(amountOfPackages, 0)
    roundedBuns = round(amountOfBunPackages, 0)
    print(f"The number of hot dog packages needed are: {roundedPackages}")
    print(f"The Number of Packages needed for the Hot Dog Buns are: {roundedBuns}")

else: 
    print(f"The number of hot dog packages needed are: {amountOfPackages}")
    print(f"The Number of Packages needed for the Hot Dog Buns are: {amountOfBunPackages}")














    