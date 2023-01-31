class Solution:
    def maxArea(self, height: List[int]) -> int:
        # first attempt: don't brute force it, instead figure out a way to 
        # find what is most likely the largest and then go from there
        # so check largest bar with furthest bar and go from there

        max = 0
        left = 0
        right = len(height) - 1
        max = min((height[left], height[right])) * (right - left)
        for i in range(len(height)):
            if(min((height[left], height[right])) * (right - left) > max):
                max = min((height[left], height[right])) * (right - left)
            if(height[left] < height[right]):
                left = left + 1
            else:
                right = right - 1
      

        return max