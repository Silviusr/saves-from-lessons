class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self):
        self.capacity = 3
        self.size = 0
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.history =[]

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        print(list(self.cache))
        if key in self.cache:
            self._remove(self.cache[key])
        node = ListNode(key, value)
        self.history.append(value)
        self.cache[key] = node
        self._add(node)
        if self.size > self.capacity:
            tail_key = self.tail.prev.key
            self._remove(self.tail.prev)
            del self.cache[tail_key]

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def _add(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
        self.size += 1

    def display(self):
        current = self.head.next
        sequence = []
        while current != self.tail:
            sequence.append(current.key)
            current = current.next
        print(sequence)
        print(self.history)


# Example usage:
cache = LRUCache()
page_sequence = [1, 2, 3, 4, 1, 3]

for page in page_sequence:
    cache.put(page, page)

cache.display()  # Output: [3, 1, 4]