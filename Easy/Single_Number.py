class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # can use a dictionary to count how many times the number appears and the one that appears a single time is our answer
        # or can use a counter to do the same thing but with less code
        collection = Counter(nums)
        return collection.most_common()[-1][0]
        