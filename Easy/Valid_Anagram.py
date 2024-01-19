class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first attempt: length has to be the same, can sort strings to make it easier to compare
        # what if we can't sort strings? can use map to store letters of first string and count how many dupes
        # then compare by decreasing count. Lastly, go through map and see if any counts are not 0

        dictionary = {}

        # add characters to dictionary and increase count by 1 for repeats
        for char in s:
            if char in dictionary:
                dictionary[char] = dictionary[char] + 1
            else:
                dictionary[char] = 1
        
        # reduce count by 1, if character doesnt exist then its not an anagram
        for char in t:
            if char not in dictionary:
                return False
            dictionary[char] = dictionary[char] - 1
        
        # check all dictionary values are 0
        for value in dictionary.values():
            if value != 0:
                return False

        return True