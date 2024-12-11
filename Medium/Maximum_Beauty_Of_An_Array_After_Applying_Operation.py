class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # create an array that is the range each number can be. 
        # do the whole start + 1 and end - 1 thingy so we can see how many overlap and get the max overlap
        # this isnt the most optimal because it take n space and there is a O(1) space solution

        starts = []
        ends = []
        for n in nums:
            starts.append(n-k)
            ends.append(n+k)
        starts.sort()
        ends.sort()

        res = 0
        count = 0
        s = 0
        e = 0
        while s < len(nums) and e < len(nums):
            if starts[s] <= ends[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            res = max(res,count)


        return res