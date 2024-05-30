class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root):
        if root is None:
            return 0
        
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return left + right + 1


if __name__ == "__main__":
    s = Solution()
    tree = TreeNode(1)

    tree.left = TreeNode(2)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right = TreeNode(3)
    tree.right.left = TreeNode(6)

    print(s.countNodes(tree))
