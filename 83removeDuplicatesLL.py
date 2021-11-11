# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next 

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        head_ = head
        
        while(head.next):
            
            while head.val == head.next.val:
                
                if head.next.next:
                    head.next = head.next.next
                else:
                    head.next = None
            
                if not head.next:
                    break
                    
            if not head.next:
                break
            else:
                head = head.next
            
        return  head_ 
