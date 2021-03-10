# 2. Add Two Numbers

# Definition for singly-linked list.

# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
# [5,6,4]

# Add Two Numbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node_1 = l1
        node_2 = l2
        len1 = 0
        len2 = 0
        while node_1 is not None:
            len1+=1
            node_1 = node_1.next
        while node_2 is not None:
            len2+=1
            node_2 = node_2.next
        if(len1>=len2):
            first = l1
            second = l2
        else:
            first = l2
            second = l1
        
        node1 = first
        node2 = second
        carry = 0
        # print(first, second)
        while node1 is not None:
            
            if(node2 is None):
                node2val = 0
            else:
                node2val = node2.val
                
            temp = node1.val + node2val + carry
            carry, val = int(temp/10), temp%10
            node1.val = val
            node1 = node1.next
            
            if(node2 is None):
                continue
            else:
                node2 = node2.next
                
        if(carry>0):
            node_ = first
            while(node_.next):
                node_=node_.next
            node_.next = ListNode(carry)
        return first
            
            
            
            
        
