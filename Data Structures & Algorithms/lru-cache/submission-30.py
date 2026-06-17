class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.right = Node(0,0)
        self.left  = Node(0,0)

        self.right.prev = self.left
        self.left.next  = self.right

    def insert_node_right(self,node):
        
        self.right.prev.next = node
        node.prev = self.right.prev

        node.next = self.right
        self.right.prev = node
    
    def remove_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev



    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove_node(self.cache[key])
        self.insert_node_right(self.cache[key])
        return self.cache[key].val
        
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        #nb logic might be a bit funny here, if error arises in put logic check here fist
        #may need to do serparte logic for kei in and key not in
        
        self.cache[key] = Node(key, value)
        self.insert_node_right(self.cache[key])

        if len(self.cache) >self.cap:
            del self.cache[self.left.next.key]
            self.remove_node(self.left.next)


        

        



        
