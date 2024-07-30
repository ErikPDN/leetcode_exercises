class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_path(root, value, path):
    if root is None:
        return False

    if root.value == value:
        return True

    path.append('L')
    if find_path(root.left, value, path):
        return True
    path.pop()

    path.append('R')
    if find_path(root.right, value, path):
        return True
    path.pop()

    return False


def getDirections(root, startValue, destValue):
    if root is None:
        return []

    start_path = []
    dest_path = []

    if not find_path(root, startValue, start_path) or not find_path(root, destValue, dest_path):
        return []

    i = 0
    while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
        i += 1

    directions = ['U'] * (len(start_path) - i) + dest_path[i:]

    return directions


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.left.left = TreeNode(3)
    root.right = TreeNode(2)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(4)

    start = 3
    dest = 6

    print(getDirections(root, start, dest))  # Output esperado: ['U', 'U', 'R', 'L']
