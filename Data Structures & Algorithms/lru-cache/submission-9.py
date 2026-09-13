class Node():
    def __init__(self, key=0, val=0, nxt=None, prev=None):
        self.key=key
        self.val = val
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dummy = Node()
        self.tail = Node()
        self.dummy.nxt = self.tail
        self.tail.prev = self.dummy

    def insert_ll(self, node):
        tmp = self.dummy.nxt
        self.dummy.nxt = node
        node.prev = self.dummy
        node.nxt = tmp
        tmp.prev = node
    
    def delete_node(self, node):
        link1 = node.prev
        link2 = node.nxt
        link1.nxt = link2
        link2.prev = link1
        node.nxt = None
        node.prv = None
        return node
    
    def get(self, key: int) -> int:
        if(key in self.cache):
            # reorder
            node = self.delete_node(self.cache[key])
            self.insert_ll(node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        
        if(key not in self.cache):
            if(len(self.cache)==self.capacity):
                lru = self.delete_node(self.tail.prev)
                del self.cache[lru.key]
        
        elif(key in self.cache):
            old_node = self.cache[key]
            self.delete_node(old_node)
        new_node = Node(key=key, val=value)
        self.insert_ll(new_node)
        self.cache[key] = new_node
