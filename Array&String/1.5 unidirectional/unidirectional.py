str1 = "pale"
str2 = "bale"

def isInsertedOrDeleteChar(str1,str2):
    set1 = set(str1)
    set2 = set(str2)

    # replace char
    if abs(len(str1) - len(str2)) == 0:
        if (len(set1.symmetric_difference(set2)) != 2):
            return False
        return True
    
    # add or remove char
    if abs(len(str1) - len(str2)) == 1:
        if len(set1.symmetric_difference(set2)) != 1:
            return False
        return True
    
    return False

