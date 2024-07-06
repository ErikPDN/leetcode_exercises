class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nodesBetweenCriticalPoints(head):
    res = [-1, -1]

    head_prev = head
    head_curr = head.next

    count_critical_points = []

    i = 1

    while head_curr.next:
        if head_curr.val < head_curr.next.val and head_curr.val < head_prev.val:
            count_critical_points.append(i)

        if head_curr.val > head_curr.next.val and head_curr.val > head_prev.val:
            count_critical_points.append(i)

        i += 1
        head_prev = head_curr
        head_curr = head_curr.next

    if i < 3 or len(count_critical_points) < 2:
        return res

    max_distance = abs(count_critical_points[-1] - count_critical_points[0])

    min_distance = float('inf')
    for j in range(1, len(count_critical_points)):
        min_distance = min(min_distance, count_critical_points[j] - count_critical_points[j - 1])

    res[0] = min_distance
    res[1] = max_distance

    return res


def print_list(head):
    current = head
    while current:
        print(current.val, end=' -> ')
        current = current.next
    print('None')


# Testando a função
if __name__ == '__main__':
    input_values = [1,3,2,2,3,2,2,2,7]
    head = ListNode(input_values[0])
    current = head
    for value in input_values[1:]:
        current.next = ListNode(value)
        current = current.next

    # Imprimindo a nova lista
    print("Lista resultante após mergeNodes:")
    print_list(head)

    print(nodesBetweenCriticalPoints(head))


# def nodesBetweenCriticalPoints(head):
#     res = [-1, -1]
#
#     head_prev = head
#     head_curr = head.next
#
#     idx_min_local = 0
#     idx_max_local = 0
#
#     max_distance = 0
#     min_distance = float('inf')
#
#     count_critical_points = []
#
#     i = 0
#
#     while head_curr.next:
#         if head_curr.val < head_curr.next.val and head_curr.val < head_prev.val:
#             idx_min_local = i
#             count_critical_points.append(i)
#
#         if head_curr.val > head_curr.next.val and head_curr.val > head_prev.val:
#             idx_max_local = i
#             count_critical_points.append(i)
#
#         if len(count_critical_points) >= 2:
#             min_distance = abs(count_critical_points[0] - count_critical_points[1])
#             max_distance = abs(count_critical_points[-1] - count_critical_points[0])
#
#         i += 1
#         head_prev = head_curr
#         head_curr = head_curr.next
#
#     if i < 3:
#         return res
#
#     res[0] = min_distance
#     res[1] = max_distance
#
#     return res