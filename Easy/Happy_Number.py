"""
Prompt:
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



"""



class Solution:
    def isHappy(self, n: int) -> bool:
        if(n == 1):
            return True
        Numsum = 0
        Checknum = 4    # 4 always loops
        counter = 0

        while(Numsum != 1):
          Numsum = 0
          for x in str(n):
            Numsum += int(x)*int(x)
            counter+=1
          if(Checknum == Numsum and counter > 2):
            return False;
          n = Numsum
          

        return True
            

"""
Notes:
the number 1 is an edge case so I have a specific if statement for it. checknum = 4 because 4 
will always loop and anything that loops goes back to 4

Constraints:
1 <= n <= 231 - 1

"""