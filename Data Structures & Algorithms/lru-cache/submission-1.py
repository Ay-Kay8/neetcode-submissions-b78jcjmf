# A key is considered used if a get or a put
# operation is called on it.
class Node:
    def __init__(self, key: int, val: int, prev=None, next=None):  # FIX: removed forward reference issue
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"Node={self.key}:{self.val}"

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {} # key: Node(val)
        self.curr_size = 0

        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
    
        node = self.map[key]

        # If already head, do nothing
        if node != self.head:  # fix: explicit check instead of node.prev
            # Disconnect node
            if node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
            else:
                # If node is tail
                self.tail = node.prev
                if self.tail:  # fix: safety check
                    self.tail.next = None

            # Move to head
            node.prev = None  # fix: must reset prev
            node.next = self.head
            if self.head:     # fix: safety check
                self.head.prev = node
            self.head = node

        return node.val
    
    def put(self, key: int, value: int) -> None:
        # fix: handle existing key
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.get(key)  # move to head
            return

        new_node = Node(key, value)

        # fix: safe initialization
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        
        # Add to Map
        self.map[key] = new_node
        self.curr_size += 1

        # Remove last entry of LL
        if self.curr_size > self.capacity:
            # Delete in Map
            del self.map[self.tail.key]

            # Delete in LL
            self.tail = self.tail.prev
            if self.tail:          # FIX: safety check
                self.tail.next = None

            self.curr_size -= 1    # FIX: decrement size

    def __str__(self):
        return str(self.map)