from collections import Counter


l = [0 , 1 , 0 , 0 , 1 , 1 , 0 , 1]

def sizes_of_ones(l : list[int]) -> list[int]:
    
    if len(l) == 0 :
        return

    n = len(l)
    prev = l[0] 
    res = [1] if prev ==1 else []
    for curr in l[1:] : 
        if curr == 1 : 
            if prev == 1 :
                # incr the size of sequance 
                res[-1] += 1 
            else :
                # inti  the size of new sequance  
                res.append(1)
        prev = curr 
    return res 


print(sizes_of_ones([1,1,1]))


def longestOnes(nums : list[int] , k : int) -> int : 
    # The idea is to find the window and then res = size of window 
    # so we can define the window with two pointers : left and right 
    # so the question to find left ? and right? => res = right - left + 1 
    # there is on condition taht each window must staisfied, it is taht the numbers
    # of zeros between left and right must be less then k 
    maxx = 0 
    l = 0 
    for r in range(len(nums)):
        if nums[r] == 0 :
            k -= 1
        while k < 0 :
            if nums[l] == 0 :
                k += 1 
            l += 1 
        maxx = max(maxx , l - r +1)
    return maxx 
