#!/bin/python
# Queue using stacks

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.isEmpty():
            raise LookupError("Stack is empty")

        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def top(self):
        return self.stack[-1]

    def clear(self):
        self.stack.clear()

class StackedQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def clear(self):
        self.s1.clear()
        self.s2.clear()

    def isEmpty(self):
        return self.s1.isEmpty()

    def isFull(self):
        return False

    def enqueue(self, value):
        if self.isFull():
            raise OverflowError("Queue is full")

        while not self.s1.isEmpty():
            v = self.s1.pop()
            self.s2.push(v)

        self.s1.push(value)

        while not self.s2.isEmpty():
            v = self.s2.pop()
            self.s1.push(v)

    def dequeue(self):
        if self.isEmpty():
            raise LookupError("Queue is empty")

        return self.s1.pop()

    def top(self):
        return self.s1.top()

    def __str__(self):
        return "%s" % (self.s1)

if __name__ == "__main__":
    queue = StackedQueue()

    assert(queue.isEmpty())
    assert(not queue.isFull())

    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    #assert(queue.isFull())
    assert(not queue.isEmpty())

    assert( queue.dequeue() == 0)

    queue.enqueue(5)
    #assert(queue.isFull())
    assert(not queue.isEmpty())

    assert( queue.dequeue() == 1)
    assert( queue.dequeue() == 2)
    assert( queue.dequeue() == 3)
    assert( queue.dequeue() == 4)
    assert( queue.dequeue() == 5)

    assert(queue.isEmpty())
    #assert(not queue.isFull())
