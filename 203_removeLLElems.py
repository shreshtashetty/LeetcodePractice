# 203. Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while not head:
            return head
        
        head_ = head
        
        while head.next:
            
            while head.next.val==val:
                
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
                
        if head_.val == val:
            return head_.next
        else:
            return  head_ 
                
