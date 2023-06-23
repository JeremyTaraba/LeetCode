class Solution:
    def trap(self, height: List[int]) -> int:
        # First attempt: Use 2 pointers. When height goes down, count how long until it goes back up using min height
        # ^ couldn't get it to work

        # Second attempt: Use a max left and max right to calculate how much water we can trap O(n) run and space
        
        sum = 0

        maxLeft = []    #highest wall from the left side
        maxRight = [None]*len(height)   #highest wall from the right side

        max = 0
        for i in range(len(height)):
            maxLeft.append(max)
            if max < height[i]:
                max = height[i]
            
        
        max = 0
        for i in range(len(height)-1, -1,-1):
            maxRight[i] = max
            if max < height[i]:
                max = height[i]
            
        
    

        for i in range(len(height)):
            x = min(maxLeft[i], maxRight[i]) - height[i]
            if(x > 0):
                sum+=x

    


        return sum

        # could optimize this with less for loops