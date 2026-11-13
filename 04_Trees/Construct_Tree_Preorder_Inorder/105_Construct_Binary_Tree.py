# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
         
        if not inorder:
            return None
        
        root_val=preorder[0]
        root=TreeNode(root_val)

        i=inorder.index(root_val)

        left_inorder=inorder[:i]
        right_inorder=inorder[i+1:]

        left_preorder=preorder[1:i+1]
        right_preorder=preorder[i+1:]

        root.left=self.buildTree(left_preorder,left_inorder)
        root.right=self.buildTree(right_preorder,right_inorder)

        return root

        
        

        