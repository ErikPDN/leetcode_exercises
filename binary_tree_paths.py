from typing import Optional, List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def binaryTreePaths(root):
    if not root:
        return []

    paths = []
    stack = [(root, str(root.val))]

    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            paths.append(path)
        if node.left:
            stack.append((node.left, path + '->' + str(node.left.val)))
        if node.right:
            stack.append((node.right, path + '->' + str(node.right.val)))

    return paths


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(5)

    print(binaryTreePaths(root))
