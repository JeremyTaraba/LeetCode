class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # first attempt: sort list and then check neighbors O(n log n)
        # could also use set() and check if it already exists in the set O(n)
        s = set()

        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)

        return False

        # second attempt: Can turn list into dictionary and increment value and see if we already added it
        # runtime is O(n) since we just go through the list once, similar to set
        dict = {}
        for n in nums:
            dict[n] = dict.get(n, 0) + 1 # get the value if it exists and add 1 if not set it to 1          
            if(dict[n]==2): # if value already exists is will be 2 or greater
                return True
       
        return False
