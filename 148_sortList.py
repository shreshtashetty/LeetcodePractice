# 148. Sort List

# Merge Sort
# Neetcode: https://www.youtube.com/watch?v=TGveA1oFhrc

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge(left,right):
    tail = dummy = ListNode()
    
    while left and right:
        if left.val<=right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    if left:
        tail.next = left
    if right:
        tail.next = right
        
    return dummy.next

def getMid(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        # split the list into 2 halves
        left = head
        right = getMid(head)
        temp = right.next
        right.next = None
        right = temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return merge(left,right)
