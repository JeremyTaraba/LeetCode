class NumArray:

    # [-2,0,3,-5,2,-1]
    # [-2,-2,1,-4,-2,-3]

    def __init__(self, nums: List[int]):
        # create a prefix sum
        self.prefix = [nums[0]]
        for i in range(1,len(nums)):
            self.prefix.append(self.prefix[i-1] + nums[i])


    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.prefix[right] - self.prefix[left-1]
        return self.prefix[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)