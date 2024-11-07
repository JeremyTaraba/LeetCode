class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(word, l, r):
            while l < r:
                if word[l] != word[r]:
                    return False
                l+=1
                r-=1
            return True



        def backtracking(index, cur):
            if index == len(s):
                res.append(cur.copy())
                return
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    cur.append(s[index:i+1])
                    backtracking(i+1, cur)
                    cur.pop()
                

        backtracking(0, [])
        return res