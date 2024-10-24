
class LRUCache:
    # will be using a hashed linked list
    # use single linked list so deleting is easier, only need to know next not prev and next

    # this version without the linked list is not the most optimal
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict(lambda: None)
        self.queue = []
        

    def get(self, key: int) -> int:
        if self.cache[key] != None:
            # make value the most recently used
            self.queue.remove(key)
            self.queue.append(key) 

            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        # if the key doesnt exist in the cache
        if(self.cache[key] == None):
            if(self.capacity <= len(self.queue)):
                # over capacity, remove LRU
                leastUsedKey = self.queue.pop(0)
                del self.cache[leastUsedKey]
            self.cache[key] = value
            self.queue.append(key)
        # else the key already exists and we want to overwrite it
        else:
            self.cache[key] = value
            self.queue.remove(key)
            self.queue.append(key) 




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)