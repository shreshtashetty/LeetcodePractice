# 61. Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def rotateOnce(head):
    first = head
    p1 = head.next
    temp = head.val

    while p1.next:
        s = p1.val
        p1.val = temp
        temp = s
        p1 = p1.next
    s = p1.val
    p1.val = temp
    first.val = s
    
    return head
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        l = 0
        p1 = head
        while p1:
            l+=1
            p1 = p1.next
        
        if k%l==0:
            return head
        
        k = k%l
        
        for i in range(k):
            head = rotateOnce(head)
        
        return head
