class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # add them up as we find them, add them to a set, when we find the repeated 
        # number don't add it. take total and subtract from what it should be to find missing number

        mySet = set()
        total = 0
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                value = grid[i][j]
                if value not in mySet:
                    total+=value
                    mySet.add(value)
                else:
                    res.append(value)
        
        actualTotal = 0
        for i in range(len(grid)*len(grid) + 1):
            actualTotal+=i

        res.append(actualTotal-total)
        return res