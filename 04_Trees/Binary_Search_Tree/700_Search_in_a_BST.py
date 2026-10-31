# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        node=root

        while node and node.val!=val:

            if node.val>val:
                node=node.left
            elif node.val<val:
                node=node.right
        
        return node

        