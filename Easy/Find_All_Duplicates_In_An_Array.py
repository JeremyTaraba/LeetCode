class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = {} #set
        dupes = [] #list

        for x in nums:
            if x not in seen:
                seen[x] = 1
            else:
                if seen[x] == 1:
                    dupes.append(x)
                seen[x] += 1
                
        return dupes