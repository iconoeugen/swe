#!/bin/python
# Circular queue

class Node:
    def __init__(self, data = None):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    def __str__(self):
        return "{ data: '%s', next: '%s'}" % (str(self._data), str(self._next))

class LinkedList():
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def len(self):
        return self._len

    def is_empty(self):
        return self._head == None

    def append(self, data):
        if not self._head:
            self._head = Node(data)
            self._tail = self._head
        else:
            self._tail.next = Node(data)
            self._tail = self._tail.next

        self._len += 1

        return self._tail

    def push(self, data):
        node = Node(data)
        node.next = self._head
        self._head = node

        self._len += 1

        return node

    def pop(self):
        if not self._head:
            return None

        node = self._head
        self._head = node.next

        if self._tail == node:
            self._tail = self._head

        node._next = None

        self._len -= 1

        return node

    def head(self):
        if not self._head:
            return None

        return self._head.data

    def tail(self):
        if not self._tail:
            return None

        return self._tail.data

    def search(self, data):
        node = self._head
        while node and node.data != data:
            node = node.next

        return node

    def delete(self, data):
        if self._head and self._head.data == data:
            return self.pop()

        prev = self._head
        node = prev.next
        while node and node.data != data:
            prev = node
            node = node.next

        if node and node.data == data:
            prev.next = node.next

            if self._tail == node:
                self._tail = prev

            node._next = None

            self._len -= 1
            return node

        return None

    def __str__(self):
        ret = "{"
        node = self._head
        while node:
            ret += str(node)
            if node.next:
                ret += ", "

        ret += "}"
        return ret

if __name__ == "__main__":
    list = LinkedList()

    assert(list.len() == 0)
    assert(list.is_empty())

    list.append(0)
    assert(list.head() == 0)
    assert(list.tail() == 0)
    assert(list.len() == 1)

    list.push(1)
    assert(list.head() == 1)
    assert(list.tail() == 0)
    assert(list.len() == 2)

    list.append(2)
    assert(list.len() == 3)
    assert(list.head() == 1)
    assert(list.tail() == 2)

    node = list.delete(0)
    assert(node.data == 0)
    assert(list.head() == 1)
    assert(list.tail() == 2)
    assert(list.len() == 2)

    node = list.pop()
    assert(node.data == 1)
    assert(list.head() == 2)
    assert(list.tail() == 2)
    assert(list.len() == 1)

    node = list.delete(2)
    assert(node.data == 2)
    assert(list.len() == 0)
    assert(list.is_empty())
