class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def get_minimum_difference(self, root):
        self.min_diff = float("inf")
        self.prev = None

        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev.val)

            self.prev = node

            inorder(node.right)

        inorder(root)
        return self.min_diff


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(236)
    t.left = TreeNode(104)
    t.left.right = TreeNode(227)
    t.right = TreeNode(701)
    t.right.right = TreeNode(911)

    print(s.get_minimum_difference(t))
