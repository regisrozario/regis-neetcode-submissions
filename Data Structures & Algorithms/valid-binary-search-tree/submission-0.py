class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root, float("-inf"), float("inf"))
    
    def helper(self, root: Optional[TreeNode], left: float, right: float) -> bool:
        if not root:
            return True
        
        if not (left < root.val < right):
            return False

        return (self.helper(root.left, left, root.val) and self.helper(root.right, root.val, right))