class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # use 2 hashsets, 1 starting from pacific coast and 1 starting from atlantic coast
        # add coordinates to corresponding sets and then check the sets. use dfs to add neighbors
        ROW, COL = len(heights), len(heights[0])

        result = set()

        pacificSet = set()
        atlanticSet = set()

        def dfs(row, col, coreSet, prev):
            if row < 0 or row == ROW or col < 0 or col == COL or (row,col) in coreSet or heights[row][col] < prev:
                return

            coreSet.add((row,col))
            dfs(row+1, col, coreSet, heights[row][col])
            dfs(row-1,col, coreSet, heights[row][col])
            dfs(row,col+1, coreSet, heights[row][col])
            dfs(row,col-1, coreSet, heights[row][col])
            
            
            
        # pacific coast
        for col in range(COL):
            dfs(0,col, pacificSet, heights[0][col])
        for row in range(ROW):
            dfs(row,0, pacificSet, heights[row][0])

        
        # atlantic coast
        for col in range(COL):
            dfs(ROW-1,col, atlanticSet, heights[ROW-1][col])
        for row in range(ROW):
            dfs(row,COL-1, atlanticSet, heights[row][COL-1])


        result = pacificSet.intersection(atlanticSet)

        return list(result)