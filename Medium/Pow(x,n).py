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



        