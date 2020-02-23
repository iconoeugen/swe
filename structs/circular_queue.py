#!/bin/python
# Circular queue

class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.clear()

    def clear(self):
        self.head = -1
        self.tail = 0

    def isEmpty(self):
        return self.head == -1

    def isFull(self):
        return self.head == self.tail

    def enqueue(self, value):
        if self.isFull():
            raise OverflowError("Queue is full")

        if self.head < 0:
            self.head = self.tail

        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        if self.isEmpty():
            raise LookupError("Queue is empty")

        ret = self.queue[self.head]
        self.head = (self.head + 1) % self.size

        # reset queue if empty
        if self.head == self.tail:
            self.clear()

        return ret

    def __str__(self):
        if self.isEmpty():
            return "[]"

        queue = []
        tail = self.tail

        if self.tail <= self.head:
            tail = (self.tail + self.size)

        for i in range(self.head, tail):
            queue.append(self.queue[i % self.size])

        return "%s" % (queue)

if __name__ == "__main__":
    queue = CircularQueue(5)

    assert(queue.isEmpty())
    assert(not queue.isFull())

    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    assert(queue.isFull())
    assert(not queue.isEmpty())
    assert(str([0,1,2,3,4]) == str(queue))

    assert( queue.dequeue() == 0)

    queue.enqueue(5)
    assert(queue.isFull())
    assert(not queue.isEmpty())
    assert(str([1,2,3,4,5]) == str(queue))

    assert( queue.dequeue() == 1)
    assert( queue.dequeue() == 2)
    assert( queue.dequeue() == 3)
    assert( queue.dequeue() == 4)
    assert( queue.dequeue() == 5)

    assert(queue.isEmpty())
    assert(not queue.isFull())
