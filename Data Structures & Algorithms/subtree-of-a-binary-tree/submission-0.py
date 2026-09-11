# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.is_same(root, subRoot):
            return True

        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    def is_same(self, root, sub_root):
        if not root and not sub_root:
            return True
        
        if not root or not sub_root or root.val != sub_root.val:
            return False
        
        return self.is_same(root.right, sub_root.right) and self.is_same(root.left, sub_root.left)
        