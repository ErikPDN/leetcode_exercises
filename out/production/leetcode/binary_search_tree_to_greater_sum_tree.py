class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    result = []

    if root is None:
        return result

    if root.left:
        result.extend(inorder(root.left))

    if root.right:
        result.extend(inorder(root.right))

    result.append(root.val)

    return result


def bstToGst(root):
    def reverse_inorder(node):
        nonlocal total_sum
        if node is None:
            return
        reverse_inorder(node.right)
        total_sum += node.val
        node.val = total_sum
        reverse_inorder(node.left)

    total_sum = 0
    reverse_inorder(root)

    return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    print(bstToGst(root))





