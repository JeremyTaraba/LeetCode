class Solution:
    def quickSelect(self,nums,l,r,k):
        pivot = nums[r] # pivot is right most element
        p = l # place it at leftmost spot

        # partition
        for i in range(l,r):
            if(nums[i] <= pivot):
                nums[i], nums[p] = nums[p], nums[i]
                p+=1
            
        nums[p], nums[r] = nums[r], nums[p] # put pivot into correct spot

        if(p > k):
            return self.quickSelect(nums,l,p-1,k)
        elif(p < k):
            return self.quickSelect(nums,p+1,r,k)
        else:
            return nums[p]



    def findKthLargest(self, nums: List[int], k: int) -> int:
        # First attempt: must be solved in O(n) time complexity 
        # so no sorting algorithms
        # Use quick select algorithm instead, basically finding the kth element while slowly
        # sorting the array O(n) average and O(n^2) worst case. 

        k = len(nums) - k # replace k with the index of where it would be in sorted array
        return self.quickSelect(nums,0,len(nums)-1, k)


