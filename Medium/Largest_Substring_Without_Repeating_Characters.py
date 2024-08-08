class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # first attempt: brute force it using a nested loop and counter for length and index
        # alternatively can use a sliding window to reduce the runtime from n^2 to n
        biggestLength = 0
        charSet = set()
        left = 0
        
        for right in range(len(s)):
            if s[right] not in charSet:
                charSet.add(s[right])
                biggestLength = max(biggestLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])

                


        return biggestLength

        