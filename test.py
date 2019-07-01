def shortestSubstring(s):
    char_dict = {}
    for idx, val in enumerate(s):
        if val in char_dict:
            pass
        else:
            char_dict[val] = idx
    maxIndex = max(char_dict,key=char_dict.get)
    array = []
    for char in s:
        if char in char_dict:
            array.append(char)
        if char == maxIndex:
            while array[0] == array[1]:
                array.pop(0)
            print(array)
            print len(array)

    
shortestSubstring("aabcceeeffgg")
    
