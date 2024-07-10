class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = {}  # {key: node}

    def get(self, key: int) -> int:
        if key in self.dic:
            # move to the head
            node = self.dic[key]
            nxt = node.next
            prev = node.prev

            prev.next = nxt
            nxt.prev = prev

            self.head.next.prev = node
            node.prev = self.head
            node.next = self.head.next
            self.head.next = node
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            # move to the head
            node = self.dic[key]
            node.val = value

            nxt = node.next
            prev = node.prev
            prev.next = nxt
            nxt.prev = prev

            self.head.next.prev = node
            node.prev = self.head
            node.next = self.head.next
            self.head.next = node

        else:
            # insert at head
            node = Node(key, value)
            self.dic[key] = node

            nxt = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = nxt
            nxt.prev = node

            # evict if necessary
            if len(self.dic) > self.size:
                node = self.tail.prev
                prev = node.prev
                prev.next = self.tail
                self.tail.prev = prev

                node.prev = None
                node.next = None
                del self.dic[node.key]
                node = None


"""
1
2-1
1-2
3-1
4-3
"""