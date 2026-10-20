
class Solution:
    def diameterOfBinaryTree(self, root):
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
