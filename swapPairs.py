# 24. Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        if not head.next:
            return head
        else:
            node1 = head
            node2 = head.next
            node1.val, node2.val = node2.val, node1.val
            node =  self.swapPairs(head.next.next)
                
        return head
        
        
