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