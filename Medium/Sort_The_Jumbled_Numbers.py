class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # use tuple to store both the new mapping and the index, reason we use index is to keep order when sorting

        pairs = []
        for i, n in enumerate(nums):
            n = str(n)
            new_value = 0
            for c in n:
                new_value *= 10
                mapped_num = mapping[int(c)]
                new_value += mapped_num
            pairs.append((new_value, i))

        pairs.sort() # sorts based on the first tuple and then if there is a tie, on the second

        res = []
        for pair in pairs:
            res.append(nums[pair[1]])

        return res

        