# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return TreeNode(val)

        node=root
        previous_node=None

        while node:
            previous_node=node

            if node.val>val:
                node=node.left
            elif node.val<val:
                node=node.right
            
        new_node=TreeNode(val)

        if new_node.val<previous_node.val:
            previous_node.left=new_node

        else:
            previous_node.right=new_node
        
        
        return root
