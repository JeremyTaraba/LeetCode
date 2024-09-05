class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # to efficiently do this, use memoization (using previous steps so u don't have to recompute everything)
        # can use a queue for this
        
        left, right = 0, 0
        ans = []
        q = collections.deque() # holds indices of the largest vals

        while right < len(nums):
            # remove smaller values from the end of q when adding a bigger one
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # remove old left value when updating left
            if left > q[0]:
                q.popleft()
            
            # dont append to ans until the r is at k length or more
            if (right+1) >= k:
                ans.append(nums[q[0]])
                left += 1 
            right += 1


        return ans