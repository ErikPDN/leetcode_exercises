# best solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


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

