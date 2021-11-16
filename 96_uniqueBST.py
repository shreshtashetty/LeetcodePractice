# 96. Unique Binary Search Trees

# Solution: https://www.youtube.com/watch?v=Ox0TenN3Zpg

class Solution:
    def numTrees(self, n: int) -> int:
        
        # Given 4 nodes, considering each value as the root node, 
        # the combinations of nodes in the left and right subtrees:-
        #
        # numTree[4] = numTree[0]*numTree[3] +
        #              numTree[1]*numTree[2] +
        #              numTree[2]*numTree[1] +
        #              numTree[3]*numTree[0] 
        
        numTree = [1]*(n+1)
        
        # 1 or 0 nodes make 1 tree
        
        for nodes in range(2, n+1):
            
            total = 0
            
            for root in range(1, nodes+1):
                
                left = root-1
                right = nodes-root
                total += numTree[left]*numTree[right]
                
            numTree[nodes] = total
            
        return numTree[n]
        
        
        
