#!/bin/python
# Doubly linked list

class Node:
    def __init__(self, data = None):
        self._data = data
        self._next = None
        self._prev = None

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

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        self._prev = prev

    def __str__(self):
        return "{ data: '%s', prev: '%s', next: '%s'}" % (
            str(self._data), str(self._next), str(self._next)
        )

class DoublyLinkedList():
    def __init__(self):
        self._front = None
        self._end = None

    def is_empty(self):
        return self._front == None

    def front(self):
        return self.front_node().data

    def front_node(self):
        if self._front == None:
            raise LookupError("List is empty")

        return self._front

    def end(self):
        if self._end == None:
            raise LookupError("List is empty")

        return self._end.data

    def end_node(self):
        return self.end_node().data

    def add_front(self, data):
        node = Node(data)
        node.next = self._front

        if self._front == None:
            self._end = node
        else:
            self._front.prev = node

        self._front = node

    def add_end(self, data):
        node = Node(data)
        node._prev = self._end

        if self._end == None:
            self._front = node
        else:
            self._end.next = node

        self._end = node

    # Initial:
    #         node.next ->                   node.next
    #  node             <-  node.next.prev
    #
    # After:
    #         node.next ->             temp        temp.next -> node.next
    #  node             <- temp.prev   temp                  <- node.next.prev
    def add_after(self, node, data):
        if not node:
            raise ValueError("Cannot add after node None")
        temp = Node(data)

        temp.next = node.next
        temp.prev = node

        node.next = temp

        if temp.next:
            temp.next.prev = temp
        else:
            self._end = temp

    # Initial:
    # node.prev                 <- node.prev
    #            node.prev.next ->            node
    #
    # node.prev                 <- temp.prev  temp                 <- node.prev
    #            node.prev.next ->            temp    temp.next    ->             node
    def add_before(self, node, data):
        if not node:
            raise ValueError("Cannot add before node None")

        temp = Node(data)

        temp.prev = node.prev
        temp.next = node

        node.prev = temp

        if temp.prev:
            temp.prev.next = temp
        else:
            self._front = temp

    def search(self, data):
        node = self._front
        while node and node.data != data:
            node = node.next

        return node

    # Initial
    #            node.prev.next ->            node   node.next ->                 node.next
    # node.prev                 <- node.prev  node             <- node.next.prev
    #
    # After
    #            node.prev.next ->                                                node.next
    # node.prev                                                <- node.next.prev
    def delete(self, node):
        if not node:
            raise ValueError("Cannot add before node None")

        if self._front == node:
            self._front = node.next

        if self._end == node:
            self._end == node.prev

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

    def forward_traverse(self):
        ret = "{"
        node = self._front
        while node:
            ret += str(node)
            if node.next:
                ret += ", "
            node = node.next

        ret += "}"
        return ret

    def backward_traverse(self):
        ret = "{"
        node = self._end
        while node:
            ret += str(node)
            if node.prev:
                ret += ", "
            node = node.prev

        ret += "}"
        return ret

if __name__ == "__main__":
    list = DoublyLinkedList()

    assert(list.is_empty())

    list.add_end(0)
    assert(list.front() == 0)
    assert(list.end() == 0)

    list.add_front(1)
    assert(list.front() == 1)
    assert(list.end() == 0)

    node = list.search(1)
    list.add_before(node, 10)
    assert(list.front() == 10)

    list.add_after(list.front_node(), 20)
    list.delete(list.front_node())
    assert(list.front() == 20)
    list.delete(list.front_node())
    assert(list.front() == 1)

    list.add_end(2)
    assert(list.front() == 1)
    assert(list.end() == 2)

    node = list.search(0)
    assert(node.data == 0)

    list.delete(node)
    assert(list.front() == 1)
    assert(list.end() == 2)

    list.delete(list.front_node())
    assert(list.front() == 2)
    assert(list.end() == 2)

    node = list.search(2)
    assert(node.data == 2)

    list.delete(node)
    assert(list.is_empty())
