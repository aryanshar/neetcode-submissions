
class Node():
    def __init__(self, key=-1,val=-1):
        self.val = val
        self.nxt = None
        self.prev = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = Node(), Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def add_node(self, node):
        rest = self.head.nxt
        node.nxt = rest
        rest.prev = node
        self.head.nxt = node
        node.prev = self.head
    
    def delete_node(self, node):
        # defaults to lru_node
        link_1 = node.prev
        link_2 = node.nxt
        link_1.nxt = link_2
        link_2.prev = link_1
        return node

    def get(self, key: int) -> int:
        if(key in self.cache):
            node = self.cache[key]
            node = self.delete_node(node)
            self.add_node(node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            node = self.cache[key]
            node = self.delete_node(node)
            node.val = value
            self.add_node(node)
            return
        if(len(self.cache)==self.capacity):
            node = self.delete_node(self.tail.prev)
            del self.cache[node.key]
        new_node = Node(key, value)
        self.add_node(new_node)
        self.cache[key] = new_node
        
        
        
        
        
