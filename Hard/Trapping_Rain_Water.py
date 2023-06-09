class Solution:
    def trap(self, height: List[int]) -> int:
        # First attempt: Use 2 pointers. When height goes down count how long until it goes back up

        left = 0
        right = 0
        length = 0
        total = 0

        for i in range(len(height)):
            if height[left] > height[i]:
                right = i
                length+=1
            elif(height[left] < height[i]):
                left = i
                total += length * 