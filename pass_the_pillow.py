class ListNode:
    def __init__(self, val=1, next=None):
        self.val = val
        self.next = next


def pass_the_pillow(n, time):
    arr = []
    i, j = 0, 1
    k = 1
    while i < time + 1:
        if k < n and j < n:
            arr.append(j)
            j += 1
            k += 1
            i += 1

        elif k == n:
            arr.append(j)
            j -= 1
            k += 1
            i += 1

        else:
            while j > 1 and i < time + 1:
                arr.append(j)
                j -= 1
                i += 1

            k = 0

    return arr[-1]


if __name__ == '__main__':
    pass


# best solution

# left_to_right = True
# pos = 1
# for i in range(1, time+1):
#     if left_to_right:
#         pos += 1
#     else:
#         pos -= 1
#     if i%(n-1) == 0:
#         left_to_right = not left_to_right
# return pos

