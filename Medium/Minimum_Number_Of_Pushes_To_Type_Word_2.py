class Solution:
    def minimumPushes(self, word: str) -> int:
        # if length is less than or equal to 8 then return length (each key is one character)
        # if length is greater than 8 then check how many unique characters there are. if less than or equal to 8 then return
        # the length. If greater than 8, size - 8 and match that to min occurrences

        count = Counter(word)
        ans = 0
        index = 0
        for cnt in reversed(sorted(count.values())):
            ans += cnt * (1 + index // 8)
            index+=1

        return ans      
        
        


        return ans
