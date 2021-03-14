# 23. Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# #Solution using min heaps
#         import heapq
#         heap = []
#         for i in lists:
#             if i != None:
#                 heapq.heappush(heap, (i.val, i))
        
#         new_head = None
#         track = None
#         while heap:
#             _ , ele = heapq.heappop(heap)
#             if ele.next != None:
#                 heapq.heappush(heap, (ele.next.val, ele.next))
#             if new_head == None:
#                 new_head = ele
#                 track = new_head
#             else:
#                 track.next = ele
#                 track = track.next
#         return new_head

def merge2Lists(list1, list2):
    if not list1 or not list2:
        return list1 or list2
    
    p1, p2 = list1, list2
    count=0
    merged = ListNode(-1)
    p3 = merged
    while(p1 and p2):
        if(p1.val<=p2.val):
                p3.next = p1
                p1 = p1.next
        elif(p2.val<p1.val):
                p3.next = p2
                p2 = p2.next
        p3 = p3.next
    p3.next = p1 or p2
    return merged.next

class Solution:
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        if(len(lists)==1):
            return lists[0]
        
        for i in range(len(lists)-1):
            lists[i+1] = merge2Lists(lists[i], lists[i+1])
        return lists[-1]
        
