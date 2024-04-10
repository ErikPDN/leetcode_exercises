class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(self, head: ListNode) -> ListNode:
        init = head
        prev = None
        while head:
            if prev and head.val == prev.val:
                prev.next = head.next
            else:
                prev = head
            head = head.next

        return init


# node10 = ListNode(3)
# node0 = ListNode(3, node10)
node1 = ListNode(1)
node2 = ListNode(1, node1)
node3 = ListNode(1, node2)

solution = Solution()
result = solution.delete_duplicates(node3)

while result:
    print(result.val, end="->")
    result = result.next
