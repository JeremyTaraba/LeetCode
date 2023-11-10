class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # using the Majority Voting Algorithm to count occurences, only works because we are guaranteed a majority element
        # runtime O(n), space O(1)
        counter = 0
        candidate = 0
        
        for i in nums:
            if candidate == i:
                counter+=1
            else:
                counter-=1
                if counter < 1:
                    candidate = i
                    counter = 1
                    
        return candidate