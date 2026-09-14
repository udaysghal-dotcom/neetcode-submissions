# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = list()
        if not root:
            return result

        first_list = list()
        first_list.append(root.val)
        result.append(first_list)
        q = list()
        q.append(root)

        while True:
            curr_list = list()
            next_q = list()
            
            while q:
                if q[0].left:
                    curr_list.append(q[0].left.val)
                    next_q.append(q[0].left) 

                if q[0].right:
                    curr_list.append(q[0].right.val)
                    next_q.append(q[0].right)
                                
                q.pop(0)

            if not next_q:
                break
            else:
                result.append(curr_list)
                q = next_q
        
        return result