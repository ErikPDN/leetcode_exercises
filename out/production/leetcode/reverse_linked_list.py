class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: [ListNode]) -> [ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head = prev
        return head


node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

# Test the solution
solution = Solution()
reversed_result = solution.reverse_list(node1)
current_node = reversed_result
while current_node:
    print(current_node.val)
    current_node = current_node.next
print(reversed_result)

