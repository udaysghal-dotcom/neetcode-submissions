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
            curr_greatest = -101
            q_len = len(q)

            for _ in range(q_len):
                node = q.popleft()
                if node:
                    if node.val > curr_greatest:
                        curr_greatest = node.val

                    q.append(node.left)                    
                    q.append(node.right)
            
            if curr_greatest != -101:
                result.append(curr_greatest)
        
        return result
        