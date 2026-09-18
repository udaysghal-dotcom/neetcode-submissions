# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val_list = []
        self.traverse(root, val_list)
        return val_list[k-1]

    def traverse(self, root, val_list):
        if not root:
            return
        
        self.traverse(root.left, val_list)
        val_list.append(root.val) # only when this runs does the list grow
        self.traverse(root.right, val_list)

        return root.val
        