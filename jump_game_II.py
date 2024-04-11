from typing import List


def jump(nums: List[int]) -> int:
    max_reachable = 0
    steps = 0
    current_reach = 0
    for i, num in enumerate(nums[:-1]):
        max_reachable = max(max_reachable, i + num)
        if i == current_reach:
            steps += 1
            current_reach = max_reachable
    return steps


if __name__ == '__main__':
    print(jump([3,4,3,2,5,4,3]))
