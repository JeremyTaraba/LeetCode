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
    
        # runtime is O(log n)  space is O(1)

        # second attempt: Make this more efficient by using bits. bitwise & n and n-1 if
        # n == pow 2 then n&n-1 will be 0. Ex: 8 = 1000 and 7 = 0111 so 1000&0111 = 0

        if(n<=0):
            return False
        return ( ( n & (n-1) )== 0)
    
        # ^ runtime is O(1) and space is O(1)