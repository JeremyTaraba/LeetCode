class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # first attempt: take index1 and subtract it from the target then search for that number
        # if we find it then that is index2, if not then move to the next number
        # ^ runtime is too long so cant do this


        # Second attempt: use left and right pointers to go over half the array in worst case
        
        left = 0
        right = len(numbers) - 1
        
       
     
        while(left < right):
            twoSum = numbers[left] + numbers[right]
            if(twoSum > target):
                right-=1
            elif(twoSum < target):
                left+=1
            else:
                return [left+1,right+1]
        
        return [0,0]
