class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balanceBST(root):
    arr = inorder(root)
    return sortArrayToBST(arr)


def inorder(root):
    nodes = []
    if root:
        nodes.extend(inorder(root.left))
        nodes.append(root.val)
        nodes.extend(inorder(root.right))

    return nodes


def sortArrayToBST(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = sortArrayToBST(arr[:mid])
    root.right = sortArrayToBST(arr[mid+1:])

    return root


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)

    balanced_root = balanceBST(root)

    print(balanced_root)