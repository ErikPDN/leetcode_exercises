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
    def is_symmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def is_mirror(left, right) -> bool:
            if not left and not right:
                return True

            if not left or not right or left.val != right.val:
                return False

            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root.left, root.right)


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode()

    values_to_insert = [1,2,2,3,4,4,3]
    for value in values_to_insert:
        tree.tree_insert(value)

    print(s.is_symmetric(tree))

