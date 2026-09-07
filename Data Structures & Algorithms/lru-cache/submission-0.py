class Node():
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.nxt = None

class DoubleLinkedList():
    def __init__(self):
        self.head = None
    def insert_top(self, node):
        if self.head==None:
            self.head = node
            return
        node.nxt = self.head
        self.head.prev = node
        self.head = node

    def reshuffle(self, node):
        if self.head==node:
            return
        curr = node
        if curr.prev:
            curr.prev.nxt = curr.nxt
        if curr.nxt:
            curr.nxt.prev = curr.prev
        #now link to the start
        curr.nxt = self.head
        if self.head:
            self.head.prev = curr
        curr.prev = None
        self.head = curr

    def size(self):
        ln = 0
        if self.head:
            last = self.head
            while(last):
                last = last.nxt
                ln += 1
        return ln

    def get_last(self):
        last = self.head
        if last==None:
            return None
        while(last.nxt):
            last = last.nxt
        return last



class LRUCache:

    def __init__(self, capacity: int):
        self.max_size = capacity
        # initialize hashmap and linkedlist of data in cache
        self.mp = {}
        self.ll = DoubleLinkedList()

    def get(self, key: int) -> int:
        # if key is in hashmap
        if(key in self.mp):
            node = self.mp[key]
            # also reshuffle linked list
            self.ll.reshuffle(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # if key already in cache/map
        if(key in self.mp):
            self.mp[key].val = value
            self.ll.reshuffle(self.mp[key])
            return
        # otherwise
        
        # if cache is filled to capacity
        if(self.ll.size()==self.max_size):
            # remove last element
            last = self.ll.get_last()
            if last.prev:
                last.prev.nxt = None
            self.mp.pop(last.key)
            del last
        # otherwise, safe to insert and update
        new_node = Node(key, value)
        self.ll.insert_top(new_node)
        self.mp[key] = new_node
        return
        
