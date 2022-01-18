# 297. Serialize and Deserialize Binary Tree

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q = deque([])
        q.append(root)
        s = ""
        
        while q:
            node = q.popleft()
            if not node:
                s+="null"+","
            else:
                s+=str(node.val)+","
            
                q.append(node.left)
            
                q.append(node.right)
      
        i = len(s)-1      
        while not s[i].isdigit():
            i-=1
        # print(s[:i+1])   
        return s[:i+1]
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0:
            return None
        
        nodes = data.split(",")
        q = deque([])
        root = TreeNode(int(nodes[0]))
        ptr = root
        q.append(ptr)
        
        i = 1
        
        while i<len(nodes):
            parent = q.popleft()
            if nodes[i].lstrip("-").isdigit():
                parent.left = TreeNode(int(nodes[i]))
                q.append(parent.left)
            if i+1>=len(nodes):
                break
            if nodes[i+1].lstrip("-").isdigit():
                parent.right = TreeNode(int(nodes[i+1]))
                q.append(parent.right)
            i+=2
            
        return root
            
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
