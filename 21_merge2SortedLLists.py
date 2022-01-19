# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l = ListNode(0)
        p_list = l
        
        p1 = l1
        p2 = l2
        
        while p1 and p2:
     
            if p1.val==p2.val:
                p_list.next = ListNode(p1.val)
                p_list = p_list.next
                p_list.next = ListNode(p2.val)
                p_list = p_list.next
                p1 = p1.next
                p2 = p2.next
                
            elif p1.val<p2.val:
                p_list.next = ListNode(p1.val)
                p_list = p_list.next
                p1 = p1.next
                
            elif p2.val<p1.val:
                p_list.next = ListNode(p2.val)
                p_list = p_list.next
                p2 = p2.next
                
      
        if p1 or p2:        
            if p1:
                rem = p1
            elif p2:
                rem = p2

            while rem:
                p_list.next = ListNode(rem.val)
                p_list = p_list.next
                rem = rem.next

        return l.next
                
        
        '''
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
            
        '''
        
