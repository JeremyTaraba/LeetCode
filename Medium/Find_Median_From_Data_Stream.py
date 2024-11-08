class MedianFinder:

    def __init__(self):
        # 2 heaps so can find middle faster
        self.min = [] # min heap, holds larger numbers
        self.max = [] # max heap, holds smaller numbers

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max, -num)

        if self.min and self.max and self.min[0] < -self.max[0]: #  move max to min
            temp = -1 * heapq.heappop(self.max)
            heapq.heappush(self.min, temp)
        
        # check that lengths are at most 1 apart
        if len(self.max) > len(self.min) + 1:
            temp = -1 * heapq.heappop(self.max)
            heapq.heappush(self.min, temp)
        if len(self.min) > len(self.max) + 1:
            temp = heapq.heappop(self.min)
            heapq.heappush(self.max, -temp)

    def findMedian(self) -> float:
        if len(self.max) > len(self.min):
            return -self.max[0]
        if len(self.max) < len(self.min):
            return self.min[0]
        return (-self.max[0] + self.min[0]) / 2
        

        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()