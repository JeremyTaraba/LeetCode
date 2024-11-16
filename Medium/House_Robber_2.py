class Solution:
    def rob(self, nums: List[int]) -> int:
        # compute solution without first value
        # compute solution without last value
        # take the max

        if len(nums) == 1:
            return nums[0]
    
        def robber1(li):
            first = 0
            second = 0
            for n in li:
                temp = max(n+first, second)
                first = second
                second = temp
                
            return second
        a = robber1(nums[1:])
        b = robber1(nums[:-1])
        return max(a,b)