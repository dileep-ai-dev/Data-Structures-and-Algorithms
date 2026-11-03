class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(preorder, inorder):
    if not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    i = inorder.index(root_val)

    left_inorder = inorder[:i]
    right_inorder = inorder[i + 1:]

    left_preorder = preorder[1:i + 1]
    right_preorder = preorder[i + 1:]

    root.left = build_tree(left_preorder, left_inorder)
    root.right = build_tree(right_preorder, right_inorder)

    return root


def inorder_traversal(root):
    if root is None:
        return []

    return (
        inorder_traversal(root.left)
        + [root.data]
        + inorder_traversal(root.right)
    )


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = build_tree(preorder, inorder)
print(inorder_traversal(root))