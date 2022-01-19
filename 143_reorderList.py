# 143. Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# split list in half, reverse 2nd list and then merge lists.

def reverseList(head):
    
    prev = None
    
    while head:
        
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
        
    return prev

def mergeLists(l1, l2):
    
    p1 = l1
    p2 = l2
    
    while p1 and p2:
        
        temp = p1.next
        p1.next = ListNode(p2.val)
        p1.next.next = temp
        p1 = p1.next.next
        p2 = p2.next
        
    return l1
    
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """  
        l = 0
        p1 = head
        
        while p1:
            l+=1
            p1 = p1.next
        
        import math
        half = math.ceil(l/2)
        
        p2 = head
        
        while half>1:
            p2 = p2.next
            half-=1
        
        list2 = p2.next
        p2.next = None
        
        list2 = reverseList(list2)
        
        head = mergeLists(head, list2)
        
        
        '''
        if not head.next or not head.next.next:
            return head
        
        ptr1 = head
        ptr2 = head.next.next
        ptr3 = head
        
        stack = []
        
        l = 1
        
        while ptr2:
            stack.append(ptr2.val)
            ptr2 = ptr2.next
            l+=1
        l+=1
  
        import copy
        l1 = copy.deepcopy(l)
        
        while ptr1.next:
            temp = ptr1.next
            ptr1.next = ListNode(stack.pop())
            ptr1.next.next = temp
            l-=2
            if l<=1:
                break
            ptr1 = ptr1.next.next

        while(l1>0):
            ptr3 = ptr3.next
            l1-=1
            if l1==1:
                ptr3.next = None
        '''
        '''
        p1 = head
        l = 0
        
        while p1:
            l+=1
            p1 = p1.next
        
        stack = []
        
        import math
        inds, inds1 = l-(math.ceil(l/2)-1), l-(math.ceil(l/2)-1)
        
        p1 = head
        
        while inds>0:
            inds-=1
            p1 = p1.next
        
        while p1:
            stack.append(p1.val)
            p1 = p1.next
        
        p1 = head   

        while stack:
            val = ListNode(stack.pop())
            temp = p1.next
            p1.next = val
            val.next = temp
            p1 = p1.next.next
            
        p1 = head  

        while l>1:
            l-=1
            p1 = p1.next

        p1.next = None   
            
        return head
        '''
            
        
        # BRUTE FORCE
#         while ptr1:
            
#             while ptr2.next.next:
#                 ptr2 = ptr2.next
            
#             temp = ptr1.next
#             ptr1.next = ListNode(ptr2.next.val)
#             ptr1.next.next = temp
#             ptr2.next = None
#             ptr1 = ptr1.next.next
            
#             if ptr1.next:
#                 ptr2 = ptr1.next
#             else:
#                 break
                
#             if not ptr2.next:
#                 break
                
        return head
