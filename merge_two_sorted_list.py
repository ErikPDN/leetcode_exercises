class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        merge_list = ListNode()
        curr = merge_list

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next