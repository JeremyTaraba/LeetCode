class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # find current mean, then add onto it unti it reaches target mean

        totalRolls = len(rolls) + n
        sumOfRolls = sum(rolls)
        curMean = sumOfRolls / totalRolls

        if curMean > mean:
            return []
        
        offset = sumOfRolls % totalRolls
        if offset != 0:
            offset = totalRolls - offset

        roundedCurMean = math.ceil(curMean)

        stillNeed = mean - roundedCurMean

        totalNeed = stillNeed * totalRolls + offset

        ans = []
        if totalNeed < n:
            return []
        if not (totalNeed / totalRolls <= 6):
            return []

        for i in range(n):
            if totalNeed > 6:
                ans.append(6)
                totalNeed -= 6
            else:
                ans.append(totalNeed)
                totalNeed = 0

        if totalNeed > 0:
            return []

        j = 0
        for i in range(n):
            if ans[i] == 0:
                if ans[j] > 1:
                    ans[j] -= 1
                    ans[i] += 1
                else:
                    j+=1
                    ans[j] -= 1
                    ans[i] += 1
            
        

        return ans


