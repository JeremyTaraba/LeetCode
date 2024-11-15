class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # create a hashmap that stores the last index each character is seen at
        # go through the list and at each character our max partition is the max of each character
        # if our max = index then we have made 1 partition, also hold a prev variable so we know where that partition
        # ended so we can calculate the size of the next partition
        res = []
        letters = {}
        for i in range(0,len(s)):
            letters[s[i]] = i
        
        maxIndex = letters[s[0]]
        partitionEnd = -1
        for i in range(0,len(s)):
            maxIndex = max(maxIndex, letters[s[i]])
            if maxIndex == i:
                res.append(maxIndex - partitionEnd)
                partitionEnd = i
            
            

        return res