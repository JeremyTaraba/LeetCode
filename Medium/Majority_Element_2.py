class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # first attempt: could use a hashmap to count how many times the numbers appear and then
        # go through the values of the map and any above n/3 will be returned as a list
        # can this be solved in O(1) space? sorting it maybe, but we want linear time
        
        size = len(nums)
        

        hashmap = {}
        ans = []

        for i in nums:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] = 1
        
        for k, v in hashmap.items():
            if v*3 > size:
                ans.append(k)
        
        return ans
    
     # second attempt: We can only return atmost, 2 elements Boyer-Moore Majority Voting Algorithm
