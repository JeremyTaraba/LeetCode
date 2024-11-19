class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # consecutive numbers to make large product.
        # keep max and min to deal with negative numbers

        maxProd = 1
        minProd = 1
        res = max(nums)
        for num in nums:
            if num != 0:
                temp = maxProd
                maxProd = max(num * maxProd, num * minProd, num)
                minProd = min(num * temp, num * minProd, num)
                res = max(res, maxProd, minProd)
            else:
                maxProd = 1
                minProd = 1
            


        return res