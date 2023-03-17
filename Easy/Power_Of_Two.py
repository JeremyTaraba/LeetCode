class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # first attempt: numbers that are powers of 2 are even and will stay an even num when you
        # divide it by 2 until it hits 2. Ex: 8/2 = 4, 4/2 = 2. 10/2 = 5 which is odd number

        if(n <= 0):
            return False
        if(n == 1 or n == 2):
            return True

        while(n%2 == 0):
            n=n/2
            if(n==2):
                return True

        return False

        # second attempt: Make this more efficient by 