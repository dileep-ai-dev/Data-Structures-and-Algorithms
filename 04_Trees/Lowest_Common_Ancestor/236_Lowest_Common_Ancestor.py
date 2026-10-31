class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def LCA_General(root, p, q):
    if root is None or root.data == p or root.data == q:
        return root

    left_search = LCA_General(root.left, p, q)
    right_search = LCA_General(root.right, p, q)

    if left_search and right_search:
        return root

    return left_search if left_search else right_search


root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

ans = LCA_General(root, 6, 4)
print(ans.data) 
