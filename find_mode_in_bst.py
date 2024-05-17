from collections import defaultdict

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def find_mode(self, root):
        modes = []
        if root is None:
            return 0

        if root.left:
            if root.left.val == root.val:
                modes.append(root.left.val)
                self.find_mode(root.left)

        if root.right:
            self.find_mode(root.right)

        return modes

    def findMode(self, root):
        if not root:
            return []

        def inorder_traversal(node: TreeNode):
            if not node:
                return
            inorder_traversal(node.left)
            count[node.val] += 1
            inorder_traversal(node.right)

        count = defaultdict(int)
        inorder_traversal(root)

        max_count = max(count.values())
        return [max_count]


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(0)

    print(s.findMode(root))