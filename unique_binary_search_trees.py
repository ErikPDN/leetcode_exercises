class Solution:
    def num_trees(self, n: int) -> int:
        if n <= 1:
            return 1

        count_tree = [0] * (n + 1)
        count_tree[0] = 1
        count_tree[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                count_tree[i] += count_tree[j - 1] * count_tree[i - j]

        return count_tree[n]


if __name__ == '__main__':
    s = Solution()
    n = 10
    print(s.num_trees(n))

