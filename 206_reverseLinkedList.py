# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        
        while head:
            
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
            
        return prev
        
        '''
        stack = deque()
        if not head:
            return head
        
        while(head):
            stack.appendleft(head.val)
            head = head.next
        
        val = stack.popleft()
        dummy_node = ListNode(val)
        head = dummy_node
        
        while(stack):
            val = stack.popleft()
            dummy = ListNode(val)
            head.next = dummy
            head = head.next
        
        return dummy_node
        '''
