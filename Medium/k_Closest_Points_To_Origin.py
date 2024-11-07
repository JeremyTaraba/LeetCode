class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        def findDistance(p):
            return math.dist(p, [0,0])

        pq = []
        
        index = 0
        for p in points:
            distance = findDistance(p)
            heapq.heappush(pq, (distance, index))
            index+=1

        for i in range(0,k):
            priority, task = heapq.heappop(pq)
            res.append(points[task])

        return res