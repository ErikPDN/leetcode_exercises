class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def tree_insert(self, val: int) -> None:
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.tree_insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.tree_insert(val)


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        depth_left = self.max_depth(root.left)
        depth_right = self.max_depth(root.right)

        return max(depth_left, depth_right) + 1


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode()

    values_to_insert = [3, 9, 20, 15, 7]
    for value in values_to_insert:
        tree.tree_insert(value)

    print(s.max_depth(tree))
