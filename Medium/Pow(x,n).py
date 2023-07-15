class Solution:
    def myPow(self, x: float, n: int) -> float:
        # first attempt: for positive n can do a loop
        # for negative n can do same loop and then divide 1 by answer
        if n == 0:
            return 1
        if n < 0:
            power = -n
        else:
            power = n

        result = 1
        for i in range(power):
            result *= x

        if n < 0:
            return 1/result

        return result

    
        # ^ run time is O(n) but is too slow


        # here is a new one with O(log n)
        negative = False
        if n == 0:
            return 1
        if n < 0: 
            negative = True
            n = -n


        result = 1

        # want to shrink n by half each time
        while n > 0:
            if n % 2 == 1:  # on odd number we can multiply result with x, will always hit n = 1 before ending loop
                result *= x

            x*=x    # increase x, exponentially
            n = n // 2 # decrease n by half each time
            

        if negative:
            return 1/result

        return result



        