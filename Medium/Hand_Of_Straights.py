class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # check if can be put into groups
        size = len(hand)
        if size % groupSize != 0:
            return False
        
        # check if is consecutive
        # put into map, start at smallest value and find if next value exists
        cards = defaultdict(int)
        handSet = set(hand)
        minHeap = list(handSet)
        heapq.heapify(minHeap)
        for value in hand:
            cards[value] += 1

               
        while minHeap:
            smallest = minHeap[0]           
            for i in range(groupSize):
                if not cards[smallest]:
                    return False
                if cards[smallest] <= 0:
                    return False
                cards[smallest] -= 1
                if cards[smallest] == 0:
                    temp = heapq.heappop(minHeap)
                    if temp != smallest:
                        return False
                smallest+=1
            
        return True
