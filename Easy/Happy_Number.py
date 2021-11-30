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
            