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
            if (r.val > p.val and r.val < q.val) or (r.val < p.val and r.val > q.val) or r.val == q.val or r.val == p.val:
                return r
            elif r.val < p.val and r.val < q.val:
                r = r.right
            else:            
                r = r.left
      