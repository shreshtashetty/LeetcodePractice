# 141. Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
1. Use two pointers, walker and runner.
2. Walker moves step by step. Runner moves two steps at time.
3. if the Linked List has a cycle walker and runner will meet at some point.
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False
        
        walker = head
        runner = head
        
        while runner.next and runner.next.next:
            walker  = walker.next
            runner = runner.next.next
            if walker==runner:
                return True
            
        return False
        
