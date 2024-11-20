class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = [0]
        visited = set()
        curSize = [0]
        def dfs(r,c):
            if (r,c) in visited or r == len(grid) or r < 0 or c < 0 or c == len(grid[0]) or grid[r][c] == 0 :
                maxArea[0] = max(maxArea[0], curSize[0])
                return
            curSize[0]+=1
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    curSize = [0]
                    dfs(i,j)



        return maxArea[0]