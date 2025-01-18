class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # record where the zeros are then go through again and set rows and columns to zero
        zerosRow = set()
        zerosCol = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zerosRow.add(r)
                    zerosCol.add(c)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in zerosRow:
                    matrix[r][c] = 0
                elif c in zerosCol:
                    matrix[r][c] = 0
        