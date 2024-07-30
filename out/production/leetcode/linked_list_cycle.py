class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        if head is None:
            return False
        
        hare = head
        tortoise = head

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if hare == tortoise:
                return True
        
        return False


if __name__ == "__main__":
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    print(Solution().hasCycle(node1))
    
    