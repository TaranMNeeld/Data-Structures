import sys

sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        return self.storage.add_to_head(value)

    def pop(self):
        current = None
        if self.storage.head:
            self.size -= 1
            current = self.storage.head.value
            self.storage.remove_from_head()
        return current

    def len(self):
        return self.size
