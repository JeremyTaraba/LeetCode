class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # use a 2 pointer approach where left = 0, right = k
        # check how many W in this range, that is the min, keep going until
        # gone through whole list. O(n*k) runtime

        left = 0
        right = k-1
        count, res = 0, k

        # i - k = 8 - 7 = 1 and block[1] == w
        # sliding window but without the initial calculation.
        # its simpler in that it will add every w and subtract every w after it has gone past k blocks
        # the res is only updated after k blocks

        for i in range(len(blocks)):
            if blocks[i] == "W":
                count+=1
            if i - k >= 0 and blocks[i-k] == "W":
                count-=1
            if i - k + 1 >= 0:
                res = min(res,count)

        return res