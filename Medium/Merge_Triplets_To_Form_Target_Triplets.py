class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # go through each indivual triplet and check indices for the correct value,
        # if the value we need has a larger value in it that we don't need then we can't use that index
        # if any value in the triplet is greater than the one we need then the whole thing is false
        # at the same time go through each list and check if the value we need is there or not
        # runtime = O(n) space = O(1)
        
        res = [False,False,False]

        for i in range(0,len(triplets)):
            num0 = triplets[i][0]
            num1 = triplets[i][1]
            num2 = triplets[i][2]

            if num0 > target[0] or num1 > target[1] or num2 > target[2]:
                continue
            if num0 == target[0]:
                res[0] = True
            if num1 == target[1]:
                res[1] = True
            if num2 == target[2]:
                res[2] = True



        return res[0] and res[1] and res[2]