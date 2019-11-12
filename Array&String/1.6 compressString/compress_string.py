sample = "aabcccccaaa"

def compressString(string):
    tempChar = string[0]
    counter = 0
    compressedString = ""
    for index, currentChar in enumerate(string):
        if index == len(string)-1:
            counter = counter + 1
            compressedString = compressedString + tempChar + str(counter)
            return compressedString
        if currentChar == tempChar:
            counter = counter + 1
        else:
            compressedString = compressedString + tempChar + str(counter)
            tempChar = currentChar
            counter = 1
    
compressString(sample)        
