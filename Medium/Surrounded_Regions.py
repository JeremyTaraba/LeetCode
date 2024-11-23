class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # instead of finding the O's in the middle, try to find the O's on the edge and those O's should not change
        # mark them and whatever is connected to them. Anything that is still an O should be an X

        def findO(r,c,visit):
            if r < 0 or c < 0 or r == len(board) or c == len(board[0]) or (r,c) in visit or board[r][c] == "X":
                return
            if board[r][c] == "O":
                board[r][c] = "S"
            visit.add((r,c))
            findO(r+1, c, visit)
            findO(r-1, c, visit)
            findO(r, c+1, visit)
            findO(r, c-1, visit)
        
        
        # go around the perimeter looking for O's mark them as "S"afe
        for r in range(len(board)):
            for c in range(len(board[0])):
                if r==0 or r==len(board)-1: # if r is first or last row
                    print(r,c)
                    if board[r][c] == "O":  # check every column
                        findO(r,c,set())
                else: # if r is not the first or last value 
                    if c == 0 or c == len(board[0])-1:    # only check first and last c
                        print(r,c)
                        if board[r][c] == "O":
                            findO(r,c,set()) # check if anything is connected to it
                
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"
