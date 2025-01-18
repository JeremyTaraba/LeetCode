class DetectSquares:

    def __init__(self):
        self.pntsCount = defaultdict(int)   # keeps track of duplicate points
        self.pts = []   # keeps track of all points we have

    def add(self, point: List[int]) -> None:
        self.pntsCount[tuple(point)]+=1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x,y in self.pts:
            if abs(py-y) != abs(px-x) or x == px or y == py:
                continue
            res += self.pntsCount[(px,y)] * self.pntsCount[(x,py)]
        return res

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)