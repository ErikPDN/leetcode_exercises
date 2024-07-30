from typing import List


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
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result

        if root.left:
            result.extend(self.postorder_traversal(root.left))

        if root.right:
            result.extend(self.postorder_traversal(root.right))

        result.append(root.val)

        return result


if __name__ == "__main__":
    s = Solution()
    tree = TreeNode()

    values_to_insert = [1, 2, 3]
    for value in values_to_insert:
        tree.insert(value)

    print(s.postorder_traversal(tree))
