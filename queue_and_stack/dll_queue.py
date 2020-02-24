import sys

sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_head(value)

    def dequeue(self):
        current = None
        if self.storage.tail:
            self.size -= 1
            current = self.storage.tail.value
            self.storage.remove_from_tail()
        return current

    def len(self):
        return self.size

