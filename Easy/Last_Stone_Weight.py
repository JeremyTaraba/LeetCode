class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lastStone = 0
        negativeStones = [] # heapify is a min heap, we want max heap so make list negative
        for val in stones:
            negativeStones.append(-val)
        heapq.heapify(negativeStones)

        while negativeStones:
            lastStone = heapq.heappop(negativeStones)
            if negativeStones:
                secondStone = heapq.heappop(negativeStones)
            else:
                break
            result = lastStone - secondStone
            heapq.heappush(negativeStones, result)


        return -lastStone