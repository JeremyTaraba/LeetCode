# First attempt: just use a list, simple
# run time for contains would be O(n) since we would use a for each loop
# actual hashtables have O(1) contains since they use a hash function to have unique look ups

class MyHashSet:

    def __init__(self):
        self.set = []
        

    def add(self, key: int) -> None:
        if(key not in self.set):
            self.set.append(key)

        

    def remove(self, key: int) -> None:
        for i in range(0,len(self.set)):
            if(self.set[i] == key):
                self.set.remove(key)
                return
        

    def contains(self, key: int) -> bool:
        if(key in self.set):
            return True
        return False
    

    # Second attempt: Trying to use a hash for O(1) lookup, bad for memory but great runtime

class MyHashSet:
    size = 262144

    def __init__(self):
        self.set = [None] * self.size  #size of table is 2048, smaller size = more likely to collide
        
        
    def hash_funct(self, key: int) -> int:
        return hash(key) % self.size 

    def add(self, key: int) -> None:
        self.set[self.hash_funct(key)] = key     

        

    def remove(self, key: int) -> None:
        self.set[self.hash_funct(key)] = None
        

    def contains(self, key: int) -> bool:
        if self.set[self.hash_funct(key)] != None:
            return True
        return False