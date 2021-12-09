# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'

class Solution:
    def changeSign(self, head: ListNode):
        while ( head ):
            head.val *= -1
            head = head.next
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        self.changeSign(headA)
        
        while ( headB ):
            if headB.val < 0:break
            headB = headB.next
        
        self.changeSign(headA)
        return headB
