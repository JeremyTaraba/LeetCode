class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # seems like a minimum spanning tree, picking the minimum from top left and bottom right
        # we just need to find the largest within that minimum tree, we go until it is connected
        # will need to use a shortest path algorithm - aka dijstras algo from (0,0) -> (n-1,n-1)
        # use a min heap to keep track of neighbors and choose the smallest one
        n = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0,0))

        # go in every direction and push the neighbors onto the heap, smallest ones will go to the front
        while minH: # guaranteed to not break out of the loop since we will hit the destination
            t, r, c = heapq.heappop(minH)
            if r== n-1 and c== n-1:
                return t
            for dr, dc in directions:
                newR, newC = r+dr, c+dc
                if (newR < 0 or newC < 0 or newR == n or newC == n or (newR,newC) in visit):
                    continue
                visit.add((newR,newC))
                heapq.heappush(minH, [max(t, grid[newR][newC]), newR, newC])
