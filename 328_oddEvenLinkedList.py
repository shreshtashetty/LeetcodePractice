# 328. Odd Even Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [1,2,3,4,5]

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        node = head
        count = 0
        if(node is None):
            return None
        
        while(node is not None):
            count+=1
            if(count==1):
                l1 = ListNode(node.val)
                node_1 = l1
                node = node.next
            if(count%2==0):
                if(count==2):
                    l2 = ListNode(node.val)
                    node = node.next
                    node_2 = l2                
                else:
                    node_2.next = ListNode(node.val)
                    node_2 = node_2.next
                    node = node.next
            elif(count%2!=0 and count!=1):
                node_1.next = ListNode(node.val)
                node = node.next
                node_1 = node_1.next
        
        node_ = l1
        if(count>1):
            while(node_.next is not None):
                node_ = node_.next
            node_.next = l2
        return l1
