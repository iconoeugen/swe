#!/bin/python
# Circular queue

# 0          x-1    x     x+1   x+2      n
#                  head   tail
#           head    0     tail               push_front(0)
#           head    0       1   tail         push_back(1)

class DoubleEndedQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.clear()

    def clear(self):
        self.head = -1
        self.tail = 0

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return self.head == self.tail

    def get_front(self):
        if self.is_empty():
            raise LookupError("Queue is empty")

        return self.queue[self.head]

    def push_front(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")

        if self.head == -1:
            self.head = self.tail = 0

        self.head = (self.size + self.head - 1) % self.size
        self.queue[self.head] = value

    def pop_front(self):
        if self.is_empty():
            raise LookupError("Queue is empty")

        node = self.queue[self.head]
        self.head = (self.head + 1) % self.size

        if self.is_full():
            self.clear()

        return node

    def get_back(self):
        if self.is_empty():
            raise LookupError("Queue is empty")

        return self.queue[(self.size + self.tail - 1) % self.size]

    def push_back(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")

        if self.head == -1:
            self.head = 0

        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.size

    def pop_back(self):
        if self.is_empty():
            raise LookupError("Queue is empty")

        self.tail = (self.size + self.tail - 1) % self.size
        node = self.queue[self.tail]

        if self.is_full():
            self.clear()

        return node

    def __str__(self):
        if self.is_empty():
            return "[]"

        queue = []
        tail = self.tail

        if self.tail <= self.head:
            tail = (self.tail + self.size)

        for i in range(self.head, tail):
            queue.append(self.queue[i % self.size])

        return "%s" % (queue)

if __name__ == "__main__":
    queue = DoubleEndedQueue(5)

    assert(queue.is_empty())
    assert(not queue.is_full())

    queue.push_front(0)

    assert(queue.get_back() == 0)
    assert(queue.get_back() == queue.get_front())

    queue.push_back(1)
    queue.push_front(2)
    queue.push_back(3)
    queue.push_front(4)

    assert(queue.is_full())
    assert(not queue.is_empty())
    assert(str([4,2,0,1,3]) == str(queue))

    assert( queue.pop_front() == 4)

    queue.push_back(5)
    assert(queue.is_full())
    assert(not queue.is_empty())
    assert(str([2,0,1,3,5]) == str(queue))

    assert( queue.pop_front() == 2)
    assert( queue.pop_back() == 5)
    assert( queue.pop_back() == 3)
    assert( queue.pop_front() == 0)
    assert( queue.pop_back() == 1)

    assert(queue.is_empty())
    assert(not queue.is_full())
