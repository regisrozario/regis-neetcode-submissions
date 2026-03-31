# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if node.val == subRoot.val and self.isValid(node, subRoot):
                return True
            if node.left: dq.append(node.left)
            if node.right: dq.append(node.right)
        
        return False

    
    def isValid(self, node: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not node and not subRoot:
            return True
        if not node or not subRoot:
            return False
        
        if node.val != subRoot.val:
            return False
        return  self.isValid(node.left, subRoot.left) and self.isValid(node.right, subRoot.right)
        