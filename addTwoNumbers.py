# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def greaterThan10(val):
    carr = val/10
    num = val%10
    return carr, num

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        numList1 = []
        numList2 = []
        carr = 0
        while l1 is not None:
            val1 = l1.val
            numList1.append(val1)
            l1 = l1.next
 
        while l2 is not None:
            val2 = l2.val
            numList2.append(val2)
            l2 = l2.next
        
        m = min(len(numList1), len(numList2))
        if len(numList1)>=len(numList2):
            sol = numList1
        else:
            sol = numList2
            
        for i in range(m):
            val1 = numList1[i]
            val2 = numList2[i]
            if val1+val2+carr>=10:
                carr, num = greaterThan10(val1+val2+carr)
                sol[i] = num
            else:
                sol[i] = val1+val2+carr
                carr=0
                
        if carr>0:
            if len(numList1)!=len(numList2):
                while carr !=0 and i<len(sol)-1:
                    a = sol[i+1]+carr
                    if a>=10:
                        carr, num = greaterThan10(a)
                        sol[i+1] = num
                        i+=1
                    else:
                        sol[i+1] = a
                        carr = 0
                    if i==len(sol)-1:
                        sol.append(carr)
                        carr = 0
                        break
            else:
                sol.append(carr)
                carr = 0
        print(sol)
        
        for i in range(len(sol)):
            sol[i] = ListNode(sol[i])
        
        l = sol[0]
        for i in range(len(sol)-1):
            sol[i].next = sol[i+1]
            
        return l
