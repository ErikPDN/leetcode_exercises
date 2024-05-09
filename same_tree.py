class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def tree_insert(self, val):
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
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)


if __name__ == '__main__':
    s = Solution()
    p = TreeNode()
    q = TreeNode()

    values_to_insert_1 = [1, 2, 3]
    values_to_insert_2 = [1, 2, 3]

    for value in values_to_insert_1:
        p.tree_insert(value)

    for value in values_to_insert_2:
        q.tree_insert(value)

    print(s.is_same_tree(p, q))
