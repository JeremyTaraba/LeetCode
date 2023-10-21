class Solution:
    def addDigits(self, num: int) -> int:
        # first attempt: can do this in a while loop O(n*digits in num)

        
            
        def addUpDigits(n):
            if n >= 9:
                return  n%10 + addUpDigits(int(n/10))
            return n

        while num - 10 >= 0:        # while theres atleast 2 digits
            num = addUpDigits(num)

        return num