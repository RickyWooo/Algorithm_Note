import sys

if len(sys.argv)<2:
    print('no argument')
    sys.exit()

def replace_char(str):     
    for char in str:
        if char == " ":
            str = str.replace(char,"%20")
    return str

replace_char(sys.argv[1])
