
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def left_boundary(root, l_boundary):
    if not root or (root.left is None and root.right is None):
        return l_boundary

    l_boundary.append(root.data)

    if root.left:
        return left_boundary(root.left, l_boundary)
    elif root.right:
        return left_boundary(root.right, l_boundary)

    return l_boundary


def right_boundary(root, r_boundary):
    if not root or (root.left is None and root.right is None):
        return r_boundary

    r_boundary.append(root.data)

    if root.right:
        return right_boundary(root.right, r_boundary)
    elif root.left:
        return right_boundary(root.left, r_boundary)

    return r_boundary


def leaf_boundary(root, boundary):
    if not root:
        return boundary

    if root.left is None and root.right is None:
        boundary.append(root.data)
        return boundary

    if root.left:
        leaf_boundary(root.left, boundary)

    if root.right:
        leaf_boundary(root.right, boundary)

    return boundary


def boundary_traversal(root):
    if not root:
        return []

    # Handle a single-node tree
    if root.left is None and root.right is None:
        return [root.data]

    left_side = left_boundary(root, [])
    leaf_nodes = leaf_boundary(root, [])
    right_side = right_boundary(root.right, [])

    return left_side + leaf_nodes + right_side[::-1]


# Create the binary tree
root = TreeNode(1)

# Left subtree of 1
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.right = TreeNode(8)
root.left.left.right.left = TreeNode(9)
root.left.left.right.right = TreeNode(10)

root.left.right = TreeNode(5)
root.left.right.left = TreeNode(14)
root.left.right.right = TreeNode(15)

# Right subtree of 1
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(11)
root.right.right.left.left = TreeNode(12)
root.right.right.left.right = TreeNode(13)

# Boundary Traversal
result = boundary_traversal(root)
print(result)
