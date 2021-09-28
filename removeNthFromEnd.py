# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        
        head_ = head
        
        while(head_.next):
            head_ = head_.next
            length+=1
        
        node_pos = length-n+1
        
        if length==1 and node_pos>0:
            return None
        
        if node_pos==1:
            head = head.next
            return head
        elif n==1:
            head_ = head
            node_pos-=1
            while(node_pos>1):
                head_ = head_.next
                node_pos-=1
            head_.next = None
            return head
        else:
            head_ = head
            node_pos-=1
            while(node_pos>1):
                head_ = head_.next
                node_pos-=1
            head_.next = head_.next.next
            return head
