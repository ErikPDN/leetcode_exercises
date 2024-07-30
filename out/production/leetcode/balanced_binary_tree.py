class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)

        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)


class Solution:
    def is_balanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        return abs(self.height(root.left) - self.height(root.right)) <= 1 and \
            self.is_balanced(root.left) and self.is_balanced(root.right)

    def height(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return max(left_height, right_height) + 1


if __name__ == '__main__':
    tree = TreeNode(10)
    tree.insert(9)
    tree.insert(20)
    tree.insert(15)
    tree.insert(7)

    s = Solution()

    print(s.is_balanced(tree))
