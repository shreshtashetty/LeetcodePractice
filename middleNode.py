# 876. Middle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 1
        
        head_ = head
        
        while(head_.next):
            head_ = head_.next
            length+=1
        
        mid_count = (length//2)
        
        while(mid_count>0):
            head = head.next
            mid_count -= 1
        
        return head
