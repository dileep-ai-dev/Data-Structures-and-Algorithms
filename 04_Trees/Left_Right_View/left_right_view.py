from collections import deque
class TreeNode:

    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


def left_right_view(root):

    if root is None:
        return []

    left=[]
    right=[]

    def main(queue1):
        if not queue1:
            return []

        queue2=[]
        left.append(queue1[0].data)
        right.append(queue1[-1].data)

        while queue1:
            num=queue1.popleft()
            if num.left:
                queue2.append(num.left)
            if num.right:
                queue2.append(num.right)

        queue1=queue2.copy()
        main(deque(queue1))

    main(deque([root]))

    return left,right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)  
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.left.right.right.right = TreeNode(9)


print(left_right_view(root))