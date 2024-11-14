class Solution:
    def jump(self, nums: List[int]) -> int:
        # first attempt: Greedy approach. See how far we can jump and check those indices, Jump to the 
        # one that is the furthest but will also take us the furthest 
        if len(nums) == 1:
            return 0
        jumps = 0
        i = 0
       
        while i < len(nums):
            jumps+=1
            biggest = 0
            index = i
            if nums[i] + i >= len(nums)-1:
                break
            for j in range(i+1,i+nums[i]+1):
                if j < len(nums) and biggest <= nums[j]+j:
                    biggest = nums[j]+j
                    index = j
            if i < index:
                i = index
            else:
                i+=1
            
        return jumps