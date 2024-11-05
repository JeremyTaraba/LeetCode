class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

    def add(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.add(w)

        ROWS = len(board)
        COLS = len(board[0])
        res, visit = set(),set()

        def dfs(r, c, node, word): # node is for the prev node in the trie, word is to keep track of what word this is
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or board[r][c] not in node.children:
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visit.remove((r,c)) # remove from visit for the next one
            

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")


        return list(res)