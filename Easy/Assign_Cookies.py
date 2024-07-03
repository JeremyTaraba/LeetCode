class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        indexG, indexS = 0, 0
        while(indexS < len(s) and indexG < len(g)):
            if(g[indexG] <= s[indexS]):
                indexG+=1
                indexS+=1
            else:
                indexS+=1

        return indexG
        