#check the 2 strings are permutation of each other or not

import sys
import string

## assume the string is composed by UNICODE

char_dict = {}

if len(sys.argv)<3:
    print('Miss arguments, valid usage: python permutation <stringA> <stringB>')
    sys.exit()

def permutation(s1,s2):
    if len(s1) != len(s2):
        return False
    for char in s1:
        char_dict[char] = True
    for char in s2:
        if not char_dict[char] :
            return False
    print("success")

permutation(sys.argv[1],sys.argv[2])