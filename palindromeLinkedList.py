# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if not head:
            return True
        
        l = []
        
        while(head):
            l.append(head.val)
            head=head.next
            
        l_rev = l[::-1]
        
        if l==l_rev:
            return True
        else:
            return False
