class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # first attempt: is s always going to be words and the pattern always characters? 
        # can turn the pattern into an array that defines the pattern and do the same with the string
        # then compare the arrays. time O(n) and space O(n+m)

        # another way to do it is using a hash table where the key is the pattern and the value is the string word
        # corresponding to the pattern character. if the value doesnt match the string then the pattern it broken
        # space and time are O(n)

        dictionary = {}
       
        # turn s into a list to make it easier, 
        s = s.split(' ')

        if len(pattern) != len(s):
            return False

        for i in range(len(pattern)):
            if pattern[i] in dictionary:
                if dictionary[pattern[i]] != s[i]:
                    return False
            else:
                dictionary[pattern[i]] = s[i]

        # check that values are unique
        values = list(dictionary.values())
        if len(values) != len(set(values)):
            return False

        return True