class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sum_of_left_leaves(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def is_leaf(node):
            return node is not None and node.left is None and node.right is None

        total_sum = 0

        if root.left:
            if is_leaf(root.left):
                total_sum += root.left.val
            else:
                total_sum += self.sum_of_left_leaves(root.left)

        if root.right:
            total_sum += self.sum_of_left_leaves(root.right)

        return total_sum

    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        total = 0
        stack = [(root, 0)]
        while stack:
            root, pos = stack.pop()
            if pos and not root.left and not root.right:
                total += root.val
            if root.left:
                stack.append((root.left, 1))
            if root.right:
                stack.append((root.right, 0))

        return total


if __name__ == '__main__':
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    print(Solution().sum_of_left_leaves(t))
    print(Solution().sumOfLeftLeaves(t))
