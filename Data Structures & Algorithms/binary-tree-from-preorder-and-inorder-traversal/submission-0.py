# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.helper(preorder,inorder,0)

    def helper(self, preorder, inorder, index =0)->Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = preorder[index]
        print(root)
        root = TreeNode(root)
        part_index = inorder.index(root.val)
        root.left = self.helper(preorder, inorder[:part_index], index+1)
        root.right = self.helper(preorder, inorder[part_index+1:], index+part_index+1)
        return root

        
        