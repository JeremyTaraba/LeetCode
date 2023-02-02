class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # First attempt: Basically sorting it but can't use sort function or create
        # a new array. Will probably just do swaps but since 0 is smallest and 2 is biggest 
        # we can use this for better optimization than normal sorting algorithm

        size = len(nums)
        left = 0
        right = size - 1
        for i in range(0,size):
            swapped = False
            while(not swapped):
                if(right < left): # checked all of them and no swap
                    left+=1
                    swapped = True
                elif(nums[left] > nums[right]): # swap them
                    temp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = temp
                right-=1
            right = size - 1

        # ^ This ended up being O(n^2) selection sort



        # Second attempt: --------------------------------------------------------------------------------
        # Since we only have 0,1,2 as our numbers we can count 
        # how many 0's, 1's, and 2's we have and then just replace the original list

        # count 0's and 1's. Don't need to count 2's cause its whatever is left
        num0 = 0
        num1 = 0
        for i in range(0,len(nums)):
            if(nums[i] == 0):
                num0 +=1
            elif(nums[i] == 1):
                num1 +=1
            

        for i in range(0,len(nums)):
            if(num0 > 0):
                nums[i] = 0
                num0-=1
            elif(num1 > 0):
                nums[i] = 1
                num1-=1
            else:
                nums[i] = 2
