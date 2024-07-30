from typing import List


class TreeNode(object):
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

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)


class Solution(object):
    def invert_tree(self, root) -> TreeNode:
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.invert_tree(root.right)
        self.invert_tree(root.left)

        return root


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(4)
    tree.insert(2)
    tree.insert(7)
    tree.insert(1)
    tree.insert(3)
    tree.insert(6)
    tree.insert(9)

    s.invert_tree(tree)
    tree.inorder(tree)


