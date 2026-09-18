# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val_list = []
        self.traverse(root, val_list, k)
        return val_list[k-1]

    def traverse(self, root, val_list, k):
        if not root or len(val_list) >= k:
            return
        
        self.traverse(root.left, val_list, k)

        if len(val_list) < k:
            val_list.append(root.val)

        self.traverse(root.right, val_list, k)
