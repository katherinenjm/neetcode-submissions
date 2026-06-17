class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.lru_counter = 0
        self.lru_curr = None
        self.capacity = capacity

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru_counter += 1
            self.cache[key][1] = self.lru_counter
            return self.cache[key][0]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        self.lru_counter += 1
        self.cache[key] = [value, self.lru_counter]

        



        if len(self.cache)>self.capacity:
            lru_key =0
            lru_curr = self.lru_counter
            for key  in self.cache:
                if self.cache[key][1] < lru_curr:
                    lru_key = key
                    lru_curr = self.cache[key][1]
            del self.cache[lru_key]



        
