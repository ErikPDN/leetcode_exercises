class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_left(self, val):
        node = ListNode(val, self.head)
        self.head = node

    def insert_right(self, val):
        if self.head is None:
            node = ListNode(val, self.head)
            self.head = node
        
        else:
            p = self.head
            while p.next:
                p = p.next

            p.next = ListNode(val)

    def print_list(self):
        curr = self.head

        while curr:
            print(curr.val, end="->")
            curr = curr.next

        print()
    
    def remove_elements(self, head, val):
        if head is None:
            return head

        curr = head
        prev = None

        while curr:
            if curr.val == val:
                if prev is None:
                    head = curr.next
                else:
                    prev.next = curr.next

            else:
                prev = curr
                
            curr = curr.next

        return head


if __name__ == "__main__":
    ll = LinkedList()
    values_to_insert = [1,2,6,3,4,5,6]
    for value in values_to_insert:
        ll.insert_right(value)

    new_list = ll.remove_elements(ll, 6)
    new_list.print_list()

