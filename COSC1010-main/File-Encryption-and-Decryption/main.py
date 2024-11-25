#
# Christian Epsinoza 
# 11/19/2024
# File Encryption and Decryption Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
# 

#Global Dictionary 
encryptionConversion = {'A':')','a':'0','B':'(','b':'9','C':'','c':'8',\
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
        '':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
        '{':'[','[':'{','}':']',']':'}'}

#Example Function Provided by Dr.T
def main():
    #Set a variable to a function. This is what if first executed in the program
    # JUMP TO THE CONVERT FUNCTION 
    result = convert()

    # AFTER RETURNING FROM THE CONVERT FUNCTION.
    #Ask the user for input. Locates the file to write to.
    fileName = input("Name of the file to encrypt to: ")
    #After the input is completed, open the selected file into write mode (deleting it's current content )
    conversionFile = open(fileName, 'w')
    #Select the file object and write out the content of the converted text (Which values are determined fromm the returned values.)
    conversionFile.write(result)

#Second part of the program. No need for arguments since we're not passing anything, the main program just deletes file contents to re-write to.
def convert():
    #Ask the user to select a file to encrypt (which will be use to encrypt the newly deleted file in the main function)
    fileNameTwo = input("File you want encrypted: ")
    #Create the ObjectName for the selected file, enter in read only mode. 
    objectForGivenText = open(fileNameTwo, 'r')
    #Set a variable to contain a string.  
    result = ''
    #Set a variable to read out the contents of the file completely.
    text = objectForGivenText.read()
    #print(text) could be used to help show was is represented in the file.
    
    #Create a loop that goes thorugh each character in the string.
    for character in text:
        #If the 
        if character.isspace():
            result+=character #Move to the next character.
        else:
            if character == encryptionConversion.values(): #Checks if the iterated character is part of the values. 
                result+=encryptionConversion.keys[character] #If so it will implement the key instead. 
            else: #If not follow the original code. 
                result+=encryptionConversion[character] 

    return result

















#The original, first attmept that was inefficent, while not used in the execution of the program, it does
#serve as a good example of what complicated code looks like.
def christianAttemptOne():

    #Remeber r is to read, w is to delete the file content and write over it. a is to open the file and to attach new content at the end. 

    #We could likely, set the file to read mode then to write mode after reading the contents.



    #Used symbols so far: @ & ! , [
    objectForGivenText = open(r'text.txt', 'r') #Open the text file. 
    
    conversionFile = open(r"encrypted.txt", 'w')

    for reading in objectForGivenText: #Reads through each Line of the file.

        for readingEachWord in reading: #For Each Line. MISUNDERSTANDING, It'll take the whole line, put it in its own sequence/classify it similar to a string, and iterate through each letter in that sequence. 
            #print(readingEachWord) this statement helps show that it's iterating through each letter rather than word.
         
            if readingEachWord == " ":
                conversionFile.write(" ")

            for testing in encryptionConversion: #For each value in the sequence, run a loop through the dictionary.

                if readingEachWord == testing: #If the iterated value is equal to the testing(a key in a dictionary), write the key-value pair to the encrypted file.
                    conversionFile.write(encryptionConversion[testing])

            #End of the Third Loop. 
        #End of the second Loop. 
    #End of the first loop
    objectForGivenText.close()
    conversionFile.close()













#This function is an updated function to the christianAttemptOne, uses the same format but new and improved for better efficency and use. 
def christianAttemptTwo():

    #Remeber r is to read, w is to delete the file content and write over it. a is to open the file and to attach new content at the end. 

    #We could likely, set the file to read mode then to write mode after reading the contents.



    #Used symbols so far: @ & ! , [
    objectForGivenText = open(r'text.txt', 'r') #Open the text file. 
    
    stringForNew = " " #Declares a String 


    fileContent = objectForGivenText.read() #Reads through each Line of the file.

    for value in fileContent: 
         
        if value.isspace():
            stringForNew+=value
        else:
            if value == encryptionConversion.values():
                stringForNew+=encryptionConversion.keys[value]
            else:
                stringForNew+=encryptionConversion[value]

            #End of the Third Loop. 
        #End of the second Loop. 
    #End of the first loop
    objectForGivenText.close()

    conversionFile = open(r"encrypted.txt", 'w')
    conversionFile.write(stringForNew)
    conversionFile.close()












#FUNCTIONS ARE CALLED HERE.
main()