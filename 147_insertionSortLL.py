# 147. Insertion Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode()
        
        curr = head
        
        while curr:
            prev_ptr = dummyNode
            next_ptr = dummyNode.next
            
            while next_ptr:
                if curr.val<next_ptr.val:
                    break
                prev_ptr = prev_ptr.next
                next_ptr = next_ptr.next
                
            temp = curr.next
            
            curr.next = next_ptr
            prev_ptr.next = curr
            
            curr = temp
            
        return dummyNode.next
