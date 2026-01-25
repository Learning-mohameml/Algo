from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)
    if n < 4 :
        return []
    nums.sort()
    res = []
    for i in range(n-3):
        if i > 0 and nums[i-1] == nums[i] : 
            continue 
        
        for j in range(i+1 ,n-2):
            if j > i+1 and nums[j -1] == nums[j] : 
                continue 
            l,r = j+1 , n-1
            while l < r :
                cand = nums[i] + nums[j] + nums[r] + nums[l]
                if cand >  target : 
                    r -= 1 
                elif cand < target : 
                    l += 1 
                else : 
                    res.append([nums[i] , nums[j],nums[r] , nums[l]])
                    l += 1 
                    r -= 1

                    while l < r and nums[l] == nums[l-1] : 
                        l += 1 
                    
                    while l <r and nums[r] == nums[r + 1] : 
                        r  -= 1 

    return res 


if __name__ == "__main__":
    # # Test 1 : 
    # nums = [-2,-1,0,0,1,2] # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    # target = 0
    # res = fourSum(nums , target)
    # print(res)

    # Test 2 : 
    nums =[2,2,2,2,2] # [[2,2,2,2]]
    target = 8
    res = fourSum(nums , target)
    print(res)
