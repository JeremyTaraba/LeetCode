class Solution:
    def mySqrt(self, x: int) -> int:
        # first attempt: try binary search
        if(x==1):
            return 1
        left = 0
        right = x//2   # can't be bigger than half the number
        while(left <= right):
            mid = left+(right - left) // 2
            if(mid*mid == x):
                return int(mid)
            if(mid*mid < x):
                left = mid+1 
            else:
                right = mid-1

        return right  # round down to nearest integer