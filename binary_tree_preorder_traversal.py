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
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result

        result.append(root.val)

        if root.left:
            result.extend(self.preorder_traversal(root.left))
        
        if root.right:
            result.extend(self.preorder_traversal(root.right))

        return result


if __name__ == "__main__":
    s = Solution()
    tree = TreeNode()

    values_to_insert = [1, 2, 3]
    for value in values_to_insert:
        tree.insert(value)

    print(s.preorder_traversal(tree))

