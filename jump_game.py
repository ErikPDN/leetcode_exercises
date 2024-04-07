def can_jump(nums):
    max_reachable_index = 0
    for i, jump in enumerate(nums):
        if i > max_reachable_index:
            return False
        if i + jump > max_reachable_index:
            max_reachable_index = i + jump
    return True



numbers = [0]
print(can_jump(numbers))

