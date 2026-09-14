# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        r = root

        while True:
            if r.val < q.val and r.val < p.val:
                r = r.right
            elif r.val > q.val and r.val > p.val:
                r = r.left
            else:
                return r
                  