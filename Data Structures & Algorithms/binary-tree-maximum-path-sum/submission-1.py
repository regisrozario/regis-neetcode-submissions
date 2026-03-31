# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]
        self.dfs(root, result)
        return result[0]

    
    def dfs(self, root, result) -> int:
        if not root:
            return 0
        
        left_max = self.dfs(root.left, result)
        right_max = self.dfs(root.right, result)
        val = root.val + max(left_max, 0) + max(right_max, 0)
        
        result[0] = max(result[0], val)
        return root.val + (max(left_max, right_max, 0))
        