class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # first attempt: use a dictionary to keep track of what we have seen so far
        # only need to go through half of the array + 1 before we can check the dictionary for dupes
        # checking for dupes could take O(n) time in worst case, doesnt have to be dictionary, could be list
        # another way to do this is using math, since you know the dupe will appear n times you can sum nums
        # then sum the set of nums and subtract and divide by n to get the dupe. runtime and space arent any better tho

        dictionary = {}

        size = len(nums)

        for i in range(0,size//2+1):
            if nums[i] in dictionary:
                return nums[i]
            else:
                dictionary[nums[i]] = 1
        return nums[size//2+1]