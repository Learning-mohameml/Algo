from typing import Optional
from pprint import pprint
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_
    def print(self , name : str = "LinkedList") :
        "LinkdedList : a -> b -> None"
        res = f"{name} : "
        ptr = self 
        while ptr : 
            res += f"{ptr.val} -> "
            ptr = ptr.next 
        res += "None"
        print(res)



def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    res = ListNode() # ListNode()
    ptr_res = res
    ptr1 = list1 
    ptr2 = list2 
    step = 0 
    while ptr1 and ptr2 :
        if ptr1.val <= ptr2.val :
            ptr_res.next = ptr1 # ListNode(ptr1.val)
            ptr1 = ptr1.next 
        else : 
            ptr_res.next = ptr2 # ListNode(ptr2.val)
            ptr2 = ptr2.next
        ptr_res = ptr_res.next         

        # print res : 
        res.print(f"Res {step}")
        step += 1 
    ptr_res.next = ptr1 or ptr2 

    return res.next
    
    
list1 = ListNode(1 , ListNode(2 , ListNode(4)))
list2 = ListNode(3 , ListNode(5  , ListNode(6)))


res = mergeTwoLists(list1 , list2)


# list1.print(name="L1")
# list2.print(name="L2")

res.print(name="Res")


# LinkedList taht has a cycle :
l1 = ListNode(3)
l2 = ListNode(2)
l3 = ListNode(0)
l4 = ListNode(-4)

l1.next = l2 
l2.next = l3 
l3.next = l4
l4.next = l2 

l1.print(name="Cycle")
