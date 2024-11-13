class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visit = set()
        def dfs(row, col, visited):
            if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == "0" or (row, col) in visited:
                return
            visited.add((row,col))
            dfs(row-1, col, visited)
            dfs(row+1, col, visited)
            dfs(row, col-1, visited)
            dfs(row,col+1, visited)

        
        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c,visit)
                    islands+=1

        return islands