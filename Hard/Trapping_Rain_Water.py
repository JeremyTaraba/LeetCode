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



        # third attempt: Use 2 pointers again but this time using min of maxLeft and maxRight - height[i]

        sum = 0

        maxLeft = height[0]   #highest wall from the left side so far
        maxRight = height[len(height)-1]   #highest wall from the right side so far
        l = 0           #left index
        r = len(height)-1      #right index

        while l <= r:
            if maxLeft < maxRight:
                x = maxLeft - height[l]
                if x < 0:
                    maxLeft = height[l]
                l+=1
               
            else:
                x = maxRight - height[r]
                if x < 0:
                    maxRight = height[r]
                r-=1
            
            if x > 0:
                sum+=x

 

        return sum

