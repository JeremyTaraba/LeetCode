class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # brute force: rot the oranges on each pass and update the grid
        # if visited every orange and one is not rotten then it is impossible

        # problem, what if we don't start at a rotting orange, what if there are mutliple rotting oranges
        # then we should do a pass through every node and look for those oranges that are rotting
        # then do another pass and keep doing passes as long as the grid is changing, max O(n*m) just to search once 
        # and can do n*m searches

        q = []
        nextQ = []
        goodOranges = [0]
        time = 0

        def spread(r,c):
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append((r,c))
            goodOranges[0]-=1

        # find initial rotten oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    goodOranges[0]+=1
                if grid[r][c] == 2:
                    q.append((r,c))

        while q and goodOranges[0] > 0:
            for i in range(len(q)):
                r,c = q.pop(0)
                spread(r+1,c)
                spread(r-1,c)
                spread(r,c+1)
                spread(r,c-1)
            time+=1
            




        return time if goodOranges[0] == 0 else -1
