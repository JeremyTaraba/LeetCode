class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # first attempt: could brute force it by dividing number by 3 and making sure it is a whole number until it reaches 1
        # is there an O(1) solution? memoization?
        if n < 1:
            return False

        while n > 1:
            if n % 3 == 0:
                n /= 3
            else:
                return False

        return True

