class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # First attempt: Use a left and right counter and add those numbers up until left > right
        # Need some way to check if we increment left or decrement right, look at next num?

        leftIndex = 0
        rightIndex = len(numbers)-1
        ans = []

        while(leftIndex < rightIndex):
            if(numbers[leftIndex] + numbers[rightIndex] == target):
                ans.append(leftIndex+1)
                ans.append(rightIndex+1)
                return ans
            elif(numbers[leftIndex] + numbers[rightIndex] < target):
                leftIndex += 1
            elif(numbers[leftIndex] + numbers[rightIndex] > target):
                rightIndex -= 1

        return ans

        # ^ is fairly optimal in both space and time O(n)