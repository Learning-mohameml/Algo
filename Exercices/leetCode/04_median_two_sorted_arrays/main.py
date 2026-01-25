from typing import List 
# Q1 : 
"""
the first Question is to implement a function that take nums list and x : int and return the 
nombre of nums[i] such as nums[i] <= x and with the constraint that the complexity O(log(n))
def count_leq(nums : List[int] , x : int) -> int : 
    ...
"""
def count_leq(nums : List[int] , x : int) -> int : 
    """
    - return the number of nums[i] <= x 
    - the idea is to use binary search in nums
    """

    left , right = 0 , len(nums)

    while left < right : 
        mid = (left + right) // 2  

        if nums[mid] <= x : 
            left = mid + 1 
        else : 
            right = mid     
    return left 



def count_geq(nums : List[int] , x : int) -> int : 
    n = len(nums)
    left , right = 0 , n
    while left < right : 
        mid = (left + right) // 2 
        if nums[mid] < x : 
            left = mid + 1 
        else : 
            right = mid
    return n - left 
            




# Q2 : 
"""
- given two listes  nums1 et nums2 already sorted and k : int 
- return the K-th smallest element in (nums1 U nums2)
- Complexity is : O(log(m+n))
"""

def kth(nums1 : List[int] , nums2 : List[int] , k :int) -> int : 
    left = min(nums1[0] , nums2[0])
    right = max(nums1[-1] , nums2[-1] )

    while left < right : 
        mid = (left + right) // 2 
        nb_inf = count_leq(nums=nums1 , x=mid) + count_leq(nums=nums2 , x=mid)

        if nb_inf <= k : 
            left = mid + 1 
        else : 
            right = mid 
    return left 

    


if __name__ == "__main__" : 
    # nums_1 = [4 , 5 , 7 , 11 , 15]
    # x = 20
    # print(f"the number of nums_1[i] <= x is {count_leq(nums_1 , x)}")

    nums1 = [4 , 5 , 7 , 11 , 15]
    nums2 = [1 , 3 , 17 , 20]
    k = 5
    print(f"the {k}-th dans nums_1 U nums_2 is {kth(nums1 , nums2 ,k)}")
    