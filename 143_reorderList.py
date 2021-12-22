# 143. Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """        
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
