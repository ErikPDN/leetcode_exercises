class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Soluition:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        
        A = headA
        B = headB

        while A != B:
            A = headB if A is None else A.next
            B = headA if B is None else B.next

        return A
    

if __name__ == "__main__":
    node1_a = ListNode(0)
    node2_a = ListNode(1)
    node3_a = ListNode(10)
    node1_a.next = node2_a
    node2_a.next = node3_a

    node1_b = ListNode(4)
    node2_b = ListNode(5)
    node3_b = ListNode(6)
    node1_b.next = node2_b
    node2_b.next = node3_b
    node3_b.next = node3_a

    print(Soluition().getIntersectionNode(node1_b, node1_a).val)

