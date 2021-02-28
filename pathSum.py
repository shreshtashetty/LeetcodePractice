class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        print(root)
        from copy import deepcopy
        tree = deepcopy(root)
        while():
            l = tree.left
            r = tree.right
            print("LEFT: {}".format(l.val))
            print("RIGHT: {}".format(r.val))
            tree = tree.right
