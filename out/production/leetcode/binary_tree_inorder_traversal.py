from typing import List


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
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result

        if root.left:
            result.extend(self.inorder_traversal(root.left))

        result.append(root.val)

        if root.right:
            result.extend(self.inorder_traversal(root.right))

        return result


if __name__ == '__main__':
    tree = TreeNode(1)

    tree.tree_insert(2)
    tree.tree_insert(3)

    s = Solution()
    print(s.inorder_traversal(tree))

