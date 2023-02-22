class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # First attempt: Can we turn it into a table that counts how many each one has occured?
        # is 3 times important? what if it was 2 times? What if we add it up and subtract by 
        # 3* each element? too complicated. Just use Counter to create a dictionary
        ans = -1
        collection = Counter(nums)

        for i in collection:
            if(collection[i] == 1):
                ans = i
        
      
                
        return ans
    
    # ^ runtime for Counter() is O(n)


    # Second attempt:       ------------------------------------------------------------
    # # Try doing a bitwise xor and & 