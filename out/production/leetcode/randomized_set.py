import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def remove(self, key):
        del self.table[key]

    def contains(self, key):
        return key in self.table


# class LinkedListWithHashTable:
#     def __init__(self):
#         self.linked_list = RandomizedSet()
#         self.hash_table = HashTable()
#
#     def insert(self, value):
#         self.linked_list.insert(value)
#         self.hash_table.insert(value, self.linked_list.head)
#
#     def remove(self, data):
#         node = self.hash_table.table.get(data)
#         if node:
#             self.linked_list.remove(data)
#             self.hash_table.remove(data)


class RandomizedSet:
    def __init__(self):
        self.hash_table = HashTable()

    def insert(self, val: int) -> bool:
        if self.hash_table.contains(val):
            return False
        else:
            self.hash_table.insert(val, True)
            return True

    def remove(self, val: int) -> bool:
        if self.hash_table.contains(val):
            self.hash_table.remove(val)
            return True
        else:
            return False

    def size(self) -> int:
        return len(self.hash_table.table)

    def get_random(self) -> int:
        random_key = random.choice(list(self.hash_table.table.keys()))
        return random_key


if __name__ == '__main__':
    linked_list = RandomizedSet()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    print(linked_list.get_random())

    # Output the linked list after removal
    current = linked_list.hash_table.table.keys()
    for val in current:
        print(val, end="->")

