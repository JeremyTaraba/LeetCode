class Solution:
    def maxProduct(self, words: List[str]) -> int:
        appears = defaultdict(set)
        words.sort(key = lambda w : len(w) )
        res = 0

        for i in range(len(words)):
            for l in words[i]:
                appears[l].add(i)

        notAppears = defaultdict(set)       # holds the index the letter does not appear in
        everyIndex = set(range(len(words)))
        for key, value in appears.items():
            notAppears[key] = everyIndex - value    # set difference
        
        for word in words:
            temp = notAppears[word[0]].copy()
            for char in word:
                temp = temp & notAppears[char]      # set intersect
            li = list(temp)
            maxTemp = max(li,default=-1)
            if maxTemp > -1:
                product = len(word) * len(words[maxTemp])
                res = max(res,product)

        return res