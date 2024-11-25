encryptionConversion = {"A": "@",  "B" : "&", "C" : "!"}

value = "A"
for reading in encryptionConversion:
    if value == reading:
        print(encryptionConversion[reading])



#What I learned:
    #looping through a dictionary, it will loop through the keys. So if you were to set the dictionary youre looping to as ".keys()" it would make no difference.


#Remember the constructor for calling a key-pair value. 
    #dictionaryName[keyName]

    