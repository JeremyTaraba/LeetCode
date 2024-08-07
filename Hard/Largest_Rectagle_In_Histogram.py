class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # find min, find area including min (by counting consecutive bars without 0), remove min.
        # ideal solution uses stack, maybe use stack to find consecutive bars
        largestArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                largestArea = max(largestArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            largestArea = max(largestArea, h * (len(heights) - i))

        return largestArea

        