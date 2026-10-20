
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree_diameter(root):
    max_path_len = [0]

    def height(node):
        if node is None:
            return 0

        left_path = height(node.left)
        right_path = height(node.right)

        max_path_len[0] = max(
            max_path_len[0], left_path + right_path
        )

        return 1 + max(left_path, right_path)

    height(root)
    return max_path_len[0]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(tree_diameter(root))  # Output: 4
