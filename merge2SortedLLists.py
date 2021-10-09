# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = l1
        p2 = l2
        l = []
        
        while p1 and p2:
            if p1.val>p2.val:
                l+=[p2.val]
                p2 = p2.next
            elif p1.val<p2.val:
                l+=[p1.val]
                p1 = p1.next
            elif p1.val==p2.val:
                l+=[p1.val, p2.val]
                p1 = p1.next
                p2 = p2.next
            
        if p1:
            while p1:
                l.append(p1.val)
                p1 = p1.next
        elif p2:
            while p2:
                l.append(p2.val)
                p2 = p2.next
        
        ll = ListNode()
        pll = ll
        for i in l:
            pll.next = ListNode(i)
            pll = pll.next
            
        return ll.next
            
