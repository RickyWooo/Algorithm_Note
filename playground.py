# s1 = "nice"
# s2 = "nicer"




# def insert_char(s1,s2):
#     if len(s2) == len(s1) + 1:
#         s1 = list(s1)
#         s2 = list(s2)
#         additional_value = s2.pop()
#         if s1 == s2:
#             print ("INSERT " + str(additional_value)) #???????


# def insert_char2(s1,s2):
#     if len(s2) == len(s1) + 1:
#         s1 = list(s1)
#         s2 = list(s2)
#         additional_value = s2.pop()
#         if s1 == s2:
#             print ("INSERT " + str(additional_value))
#     else:
#         return -1
# insert_char(s1,s2)

# def remove_char(s1,s2):
#     list(s1).reverse()
#     list(s2).reverse()
#     insert_char(s1,s2)


# def swap_char(s1,s2):
#     if len(s1) == len(s2):
#         # swap char in s1 and check if equal to s2 
#         for i in range(len(s1)):
#             for j in range(0,i):
#                 if s1[i] == s2[j]:
#                     return ("SWAP " + str(s1[i]) + str(s2[j]))

# # (s1,s2)

def swap_char(s1,s2):
    if len(s1) == len(s2):
        # swap char in s1 and check if equal to s2 
        for i, element in enumerate(s1):
            j = i + 1
            for j, element in enumerate(s1):
                s1.replace(s1[i],s1[j])
                s1.replace(s1[j],s1[i])
                if s1 == s2:
                    print("s")
                else:
                    s1.replace(s1[i],s1[j])
                    s1.replace(s1[j],s1[i])
            
    else:
        return -1
swap_char("late","tale")
