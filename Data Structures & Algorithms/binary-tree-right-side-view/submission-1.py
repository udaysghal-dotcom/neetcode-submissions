# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        
        q = collections.deque()
        q.append(root)

        while q:
            q_len = len(q)
            level = []

            for _ in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.right)
                    q.append(node.left)
                
            if level:
                result.append(level[0])
                
        return result
