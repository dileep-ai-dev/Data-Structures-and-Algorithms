
class Solution:
    def isBalanced(self, root):
        def check_balance(node):
            if node is None:
                return 0

            left_height = check_balance(node.left)
            right_height = check_balance(node.right)

            if left_height == -1 or right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        return check_balance(root) != -1
