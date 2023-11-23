class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # first attempt: try to use a binary search to find if the number exists
        # Ex: num = 16 try 16/2 = 8*8 = 64 too big so try 8/2 = 4*4 = 16
        # Ex: num = 14 try 14/2 = 7*7 = 49 too big so try 7//2 = 3*3 = 9 too small try 3+7/2  too big
        

        l = 0
        r = num
    

        while l <= r:
            mid = l + (r-l)//2
            temp = mid*mid
            if temp == num:
                return True
            if temp < num:
                l = mid+1
            if temp > num:
                r = mid-1
        return False
