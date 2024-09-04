class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merging the arrays will take O(m+n) which is longer than O(log(m+n))
        # if we cant merge them then we can take the length of the array and 

        smaller, larger = nums1, nums2
        total = len(smaller) + len(larger)
        half = total // 2

        if len(smaller) > len(larger):
            smaller, larger = larger, smaller

        l, r = 0, len(smaller) - 1
        while True:
            smallerMid = (l + r) // 2
            largerMid = half - smallerMid - 2

            smallerLeft = smaller[smallerMid] if smallerMid >= 0 else float("-inf")
            smallerRight = smaller[smallerMid + 1] if smallerMid + 1 < len(smaller) else float("inf")
            largerLeft = larger[largerMid] if largerMid >= 0 else float("-inf")
            largerRight = larger[largerMid+1] if largerMid + 1 < len(larger) else float("inf")

            if smallerLeft <= largerRight and largerLeft <= smallerRight:
                # odd total
                if total % 2:
                    return min(smallerRight, largerRight)
                return ( max(smallerLeft, largerLeft) + min(smallerRight, largerRight) ) / 2
            elif smallerLeft > largerRight:
                r = smallerMid - 1
            else:
                l = smallerMid + 1


