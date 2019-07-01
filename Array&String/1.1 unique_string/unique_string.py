import sys
import string

## assume the string is composed by ASCII CODE

if len(sys.argv)<2:
    print('no argument')
    sys.exit()

my_char_dict = {}

def dict_init():
    for char in string.printable:
        my_char_dict[char] = 0

def is_unique_string(s):
    if len(s) > 128:
        return False
    for char in s:
        if my_char_dict[char] == 1:
            print("This is not an unique string")
            return False
        else:
            my_char_dict[char] = my_char_dict[char] + 1
    print("This is unique stirng")

dict_init()
is_unique_string(sys.argv[1])


