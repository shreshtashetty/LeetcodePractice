#429. N-ary Tree Level Order Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if(root == None):
            return []
        else:
            l = []
            q = []
            count = 0
            level = 1

            while(True):

                if(isinstance(root, list)):
                    for i in range(len(root)):
                        q.append((level, root[i]))
                    #q.extend((level, root))
                else:
                    q.append((level, root))

                if(q==[]):
                    break
                    
                r = q.pop(0)
                if(len(l)<r[0] or l==[]):
                    s = []
                    s.append(r[1].val)
                    l.append(s)
                else:
                    l[r[0]-1].append(r[1].val)
                root = r[1].children
                level = r[0]+1
            
        #print(l)
        return(l)
            
            
            
            # if(isinstance(root, list)):
            #     q.extend(root)
            # else:
            #     q.append(root)
            # r = q.pop(0)
            # l.append(r.val)
            # root = r.children
            # print(l)
            
