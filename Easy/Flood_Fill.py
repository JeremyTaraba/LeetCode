class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        baseColor = image[sr][sc]
        def dfs(r,c,visited):
            if r < 0 or c < 0 or r == len(image) or c == len(image[0]) or (r,c) in visited or image[r][c] != baseColor:
                return
            visited.add((r,c))
            image[r][c] = color
            dfs(r-1,c,visited)
            dfs(r+1,c,visited)
            dfs(r,c-1,visited)
            dfs(r,c+1,visited)
        dfs(sr,sc, visited)

        return image