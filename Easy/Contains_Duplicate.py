class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # first attempt: sort list and then check neighbors
        # could also use set() and check if it already exists in the set
        s = set()

        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)

        return False

        