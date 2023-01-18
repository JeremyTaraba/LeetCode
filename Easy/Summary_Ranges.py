class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        listRanges = []
        if(len(nums) == 0):
            return listRanges
   

        startingNum = nums[0]
        endingNum = nums[0]

        for i in range(0, len(nums)-1):
            if(nums[i]+1 == nums[i+1]):
                endingNum = nums[i+1]
            else:
                if(startingNum == endingNum):
                    listRanges.append(str(startingNum))
                else:
                    listRanges.append( str(startingNum) + "->" + str(endingNum) )
                startingNum = nums[i+1]
                endingNum = nums[i+1]

        if(startingNum == endingNum):
            listRanges.append(str(startingNum))
        else:
            listRanges.append( str(startingNum) + "->" + str(endingNum) )

        return listRanges