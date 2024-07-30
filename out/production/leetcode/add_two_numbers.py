class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1, l2):
        if l1 is None and l2 is None:
            return ListNode()

        total_l1 = 0
        i = 0
        while l1:
            total_l1 += l1.val * 10**i
            i += 1
            l1 = l1.next

        total_l2 = 0
        i = 0
        while l2:
            total_l2 += l2.val * 10 ** i
            i += 1
            l2 = l2.next

        total = total_l1 + total_l2
        if total == 0:
            return ListNode()

        head = ListNode()
        curr = head

        while total > 0:
            digite = total % 10
            total //= 10
            curr.next = ListNode(digite)
            curr = curr.next

        return head.next


node1 = ListNode(3)
node2 = ListNode(4, node1)
node3 = ListNode(2, node2)

node10 = ListNode(4)
node11 = ListNode(6, node10)
node12 = ListNode(5, node11)


solution = Solution()
result = solution.add_two_numbers(node3, node12)
while result:
    print(result.val, end="")
    result = result.next


# best solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = ListNode()
#         cur=dummy
#
#         carry = 0
#         while l1 or l2 or carry:
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0
#
#             # new digit
#             val = v1 +v2 + carry
#             carry = val // 10
#             val = val % 10
#             cur.next = ListNode(val)
#
#             #update ptrs
#             cur = cur.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#
#         return dummy.next

