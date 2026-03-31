# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        final_result = []
        dq = deque([root])
        while dq:
            curr = []
            for _ in range(len(dq)):
                node = dq.popleft()
                curr.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            final_result.append(curr)
            
        return final_result