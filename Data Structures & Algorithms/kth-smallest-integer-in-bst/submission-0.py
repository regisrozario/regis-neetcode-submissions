# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.helper(root, [])[k-1]
    
    def helper(self, node:Optional[TreeNode], result:list[int]) -> list:
        if not node:
            return []
        self.helper(node.left, result)
        result.append(node.val)
        self.helper(node.right, result)
        return result