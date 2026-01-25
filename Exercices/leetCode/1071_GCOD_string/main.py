"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""


def is_gcod(str1 : str , str2 : str) :
    if str2 not in str1 : 
        return False 
    
    if len(str1) % len(str2) != 0 :
        return False 
    
    for i in range(0 , len(str1) , len(str2)):
        if str1[i : i + len(str2)] != str2 :
            return False 

    return True 

str1 = "ABAB"
str2 = "AB"

print(is_gcod(str1 , "AB"))
print(is_gcod(str1 , "A"))
print(is_gcod(str1 , "B"))
print(is_gcod(str1 , "C"))
print(is_gcod(str1 , "ABA"))



def getAllPrefix(str2 : str) -> list[str]:
    list_prefix = [
        str2[ :i] for i in range(1 , len(str2) + 1)
    ]
    
    return list_prefix
    
str2 = "AB"

print(getAllPrefix(str2))

def gcdOfStrings(str1: str, str2: str) -> str:

    if len(str1) < len(str2) : 
        str1 , str2 = str2 , str1 
    
    # list_prefix = getAllPrefix(str2)
    list_prefix = [
        str2[ :i] for i in range(1 , len(str2) + 1)
    ]

    list_gcod = []

    for prefix in list_prefix :
        if is_gcod(str1 , prefix):
            list_gcod.append(prefix)
    
    if len(list_gcod) == 0 :
        return ""
    
    return list_gcod[-1]

# str1 = "ABABABAB"
# str2 = "ABAB"

str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

print(gcdOfStrings(str1 , str2))