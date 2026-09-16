# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    good = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, root.val)
        return self.good

    def dfs(self, root, max_val):
        if not root:
            # sucessfully reach bottom without finding smaller node
            return -101

        if root.val >= max_val:
            self.good += 1
            max_val = root.val
        
        left = self.dfs(root.left, max_val)
        right = self.dfs(root.right, max_val)

        if root.val < max_val:
            # exit early, bad node
            return False 
        
        return True
