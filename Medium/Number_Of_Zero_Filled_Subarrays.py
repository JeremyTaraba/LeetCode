class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # first attempt: just count, try not to use extra space
        total = 0
        length = len(nums)
        i = 0
        while i < length:        
            if nums[i]==0:
                subarrayLength = 1
                while(subarrayLength + i < length):
                    if(nums[subarrayLength + i] == 0):
                        subarrayLength+=1
                    else:
                        break
                i += subarrayLength
                total+=sum(range(subarrayLength+1))
            i+=1
            




        return total


        
        