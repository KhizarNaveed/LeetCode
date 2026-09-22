# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## First Problem of DSA in Python

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
    
        while curr is not None:
            next_temp = curr.next  # Save the rest of the chain
            curr.next = prev       # Reverse the arrow
            prev = curr            # Move prev forward
            curr = next_temp       # Move curr forward

        return prev        


        