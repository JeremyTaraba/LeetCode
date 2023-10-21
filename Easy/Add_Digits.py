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
        

         # second attempt: There is an O(1) solution that uses a method called Digital Root and casting out 9's

        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num%9