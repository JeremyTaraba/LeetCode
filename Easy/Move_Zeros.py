class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # first attempt: theoretically can do this in O(n) time, one way to do it is using 2 pointers
        # 1 pointer on the zero and another on where next number is and then replace the zero with 
        # the next number, do this until the end of the list then go back and add zeros onto the end if it

        # another way to do this is to brute force it by finding zero then finding the next number and swapping
        
        # pointers for 0's and numbers
        l = -1
        r = 0

        # counter for zero
        zeroCounter = 0

        size = len(nums)

        
        while r < size:
            if nums[r] == 0:
                zeroCounter+=1
                if l == -1:
                    l = r
            else:
                if l != -1:
                    nums[l] = nums[r]
                    l+=1
            r+=1

        # adding zeros to the end    
        size-=1
        for i in range(zeroCounter):
            nums[size] = 0
            size-=1




        



        