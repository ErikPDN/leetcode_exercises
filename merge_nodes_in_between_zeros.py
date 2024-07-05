class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeNodes(head):
    new_head = ListNode()
    curr_new = new_head

    curr = head.next
    _sum = 0

    while curr:
        _sum += curr.val

        if curr.val == 0:
            new_node = ListNode(_sum)
            curr_new.next = new_node
            curr_new = new_node
            _sum = 0

        curr = curr.next

    return new_head.next


def print_list(head):
    current = head
    while current:
        print(current.val, end=' -> ')
        current = current.next
    print('None')


# Testando a função
if __name__ == '__main__':
    # Construindo a lista de entrada [0,3,1,0,4,5,2,0]
    input_values = [0, 3, 1, 0, 4, 5, 2, 0]
    head = ListNode(input_values[0])
    current = head
    for value in input_values[1:]:
        current.next = ListNode(value)
        current = current.next

    # Chamando a função mergeNodes
    new_head = mergeNodes(head)

    # Imprimindo a nova lista
    print("Lista resultante após mergeNodes:")
    print_list(new_head)
