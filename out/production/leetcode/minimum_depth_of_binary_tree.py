class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val) -> None:
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
    def min_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left = self.min_depth(root.left)
        right = self.min_depth(root.right)

        if (left == 0) or (right == 0):
            return max(left, right) + 1

        return min(left, right) + 1


if __name__ == "__main__":
    s = Solution()
    tree = TreeNode()

    values_to_insert = [2, 3, 4, 5, 6]
    for value in values_to_insert:
        tree.insert(value)

    print(s.min_depth(tree))
