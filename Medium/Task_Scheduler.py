class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use a max heap and pop off the largest task and decrement it. don't push it back on until n items are popped off
        # use a hash to count the occurences
        res = 0
        heap = []
        occur = defaultdict(int)

        for char in tasks:
            occur[char] +=1
        
        for key, value in occur.items():
            heapq.heappush(heap, -value)

        queue = []        
        while heap or queue:
            res+=1
            if heap:
                value = heapq.heappop(heap) + 1
                if value:
                    queue.append((value, res + n))
            if queue and queue[0][1]==res:
                temp = queue.pop(0)
                heapq.heappush(heap, temp[0])
            

        return res