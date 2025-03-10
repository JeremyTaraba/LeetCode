class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # go through both, incrementing by 1 and seeing if it matches the id, if reach the end of one then
        # append the rest of the other to the end

        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                res.append( [nums1[i][0], nums1[i][1] + nums2[j][1]] )
                i+=1
                j+=1
            elif nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1

        if i == len(nums1) and j != len(nums2):
            for arr in nums2[j:]:
                res.append(arr)
        if i != len(nums1) and j == len(nums2):
            for arr in nums1[i:]:
                res.append(arr)

        return res