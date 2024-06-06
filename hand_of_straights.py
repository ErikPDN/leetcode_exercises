def isNStraightHand(hand, groupSize):
    if (len(hand) % groupSize) != 0:
        return False

    hand.sort()
    len_groups = len(hand) // groupSize
    group = [[] for _ in range(len_groups)]
    for i in range(len_groups):
        j = 0
        k = 0
        while k < len(hand) and len(group[i]) < groupSize:
            if not group[i]:
                group[i].append(hand.pop(0))
                continue
            if hand[k] == group[i][j]+1:
                group[i].append(hand.pop(k))
                j += 1
                continue
            k += 1

    for i in range(len_groups):
        if len(group[i]) != groupSize:
            return False

    return True


hd = [2, 1]
group = 2
print(isNStraightHand(hd, group))


# best solution
# import heapq
# from collections import Counter
#
#
# def can_rearrange_into_groups(hand, groupSize):
#     if len(hand) % groupSize != 0:
#         return False
#
#     card_count = Counter(hand)
#     min_heap = list(card_count.keys())
#     heapq.heapify(min_heap)
#
#     while min_heap:
#         first = min_heap[0]
#
#         for card in range(first, first + groupSize):
#             if card_count[card] == 0:
#                 return False
#             card_count[card] -= 1
#             if card_count[card] == 0:
#                 if card != min_heap[0]:
#                     return False
#                 heapq.heappop(min_heap)
#
#     return True

