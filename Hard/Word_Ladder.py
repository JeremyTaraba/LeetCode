class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)

        hashMap = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                hashMap[pattern].append(word)
        
        visit = set()
        visit.add(beginWord)
        queue = []
        queue.append(beginWord)
        res = 1
        while queue:
            for i in range(len(queue)):
                temp = queue.pop(0)
                if temp == endWord:
                    return res
                for j in range(len(temp)):
                    pattern = temp[:j] + "*" + temp[j+1:]
                    for nei in hashMap[pattern]:
                        if nei not in visit:
                            queue.append(nei)
                            visit.add(nei)
            res+=1

        return 0
