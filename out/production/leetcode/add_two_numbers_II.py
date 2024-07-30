class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def add_two_numbers_2(l1: ListNode, l2: ListNode):
        prev = None
        cur = l1
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head = prev

        l1 = head

        prev = None
        cur = l2
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head = prev

        l2 = head

        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        prev = None
        cur = dummy.next
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        dummy = prev

        return dummy


if __name__ == "__main__":
    node0 = ListNode(3)
    node1 = ListNode(4, node0)
    node2 = ListNode(2, node1)
    node3 = ListNode(7, node2)

    node10 = ListNode(4)
    node11 = ListNode(6, node10)
    node12 = ListNode(5, node11)

    solution = Solution()
    result = solution.add_two_numbers_2(node3, node12)
    while result:
        print(result.val, end="")
        result = result.next

