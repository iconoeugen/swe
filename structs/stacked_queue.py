#!/bin/python
# Stack using queue

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if self.is_empty():
            raise LookupError("Stack is empty")

        return self.queue.pop()

    def enqueue(self, value):
        self.queue.insert(0, value)

    def top(self):
        return self.queue[-1]

    def clear(self):
        self.queue.clear()

class QueuedStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def clear(self):
        self.q1.clear()
        self.q2.clear()

    def is_empty(self):
        return self.q1.is_empty()

    def is_full(self):
        return False

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack is full")

        while not self.q1.is_empty():
            v = self.q1.dequeue()
            self.q2.enqueue(v)

        self.q1.enqueue(value)

        while not self.q2.is_empty():
            v = self.q2.dequeue()
            self.q1.enqueue(v)

    def pop(self):
        if self.is_empty():
            raise LookupError("Queue is empty")

        return self.q1.dequeue()

    def top(self):
        return self.q1.top()

    def __str__(self):
        return "%s" % (self.q1)

if __name__ == "__main__":
    stack = QueuedStack()

    assert(stack.is_empty())
    assert(not stack.is_full())

    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    #assert(queue.isFull())
    assert(not stack.is_empty())

    assert( stack.pop() == 4)

    stack.push(5)
    #assert(queue.isFull())
    assert(not stack.is_empty())

    assert( stack.pop() == 5)
    assert( stack.pop() == 3)
    assert( stack.pop() == 2)
    assert( stack.pop() == 1)
    assert( stack.pop() == 0)

    assert(stack.is_empty())
    #assert(not queue.isFull())
