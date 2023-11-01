class Solution:
    def canWinNim(self, n: int) -> bool:
        # first attempt: Sounds like a greedy approach
        # seems like there are certain numbers where you always win and some where you always lose
        # < 3 you win, 4 lose, 5 win, 6 win, 7 win, 8 lose, 9 win, 10 win multiples of 4 you lose?

        return not n % 4 == 0
        

        