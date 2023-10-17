class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # first attempt: brute force it using a nested loop and counter for length and index
        # alternatively can use a sliding window to reduce the runtime from n^2 to n

        seenChars = {}
        startIndex = 0
        biggestLength = 0

        for endIndex in range(len(s)):
            if s[endIndex] in seenChars and seenChars[s[endIndex]] >= startIndex:
                startIndex = seenChars[s[endIndex]] + 1
            else:
                biggestLength = max(biggestLength, endIndex - startIndex+1)
            seenChars[s[endIndex]] = endIndex

        return biggestLength

        