class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # since you can swap as many times as you want this is just sorting algo
        # only way it doesnt work is if target and arr are different
        # can instead do two defaultdict where the default is 0 and any hits will increment by 1 for each array
        # then go through the dict and make sure all values are the same
        # could alternatively use a single dictionary where you increment for target values and then decrement for arr values
       
        return Counter(target) == Counter(arr) # counter makes a dict that counts the occurrences of nummbers
        