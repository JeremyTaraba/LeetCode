class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # first attempt: want to use binary search, when we found the target, move up and down 
        # so we can find the beginning position and end position. Create a function that does binary search but
        # returns the left most index so we can use it for left and use it for right + 1

        def binarySearch(myTarget):
            left = 0
            right = len(nums)

            while right > left:
                i = int((right + left) // 2)
                if nums[i] < myTarget:
                    left = i+1
                else:
                    right = i           # don't do i-1 because we want right to equal left to exit loop
                    
            return left

        

        begin = binarySearch(target)     
        end = binarySearch(target+1)-1      # will give left most index of 1 more than target, so reduce it by 1 to get rightmost


        
        print(begin)
        print(end)
           

        if begin > end:
            return [-1,-1]

        return [begin,end]