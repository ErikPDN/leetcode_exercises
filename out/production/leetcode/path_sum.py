class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def has_path_sum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False

        paths = []
        stack = [(root, root.val)]

        while stack:
            node, soma = stack.pop()
            if not node.left and not node.right:
                paths.append(soma)
            if node.left:
                stack.append((node.left, soma + node.left.val))
            if node.right:
                stack.append((node.right, soma + node.right.val))

        if target not in paths:
            return False

        return True


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(5)
    t.left = TreeNode(4)
    t.left.left = TreeNode(11)
    t.left.left.left = TreeNode(7)
    t.left.left.right = TreeNode(2)
    t.right = TreeNode(8)
    t.right.left = TreeNode(13)
    t.right.right = TreeNode(4)
    t.right.right.right = TreeNode(1)

    print(s.has_path_sum(t, 22))


