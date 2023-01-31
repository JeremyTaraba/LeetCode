class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
       
        # first try: flip the matrix up and then swap things over horizontal axis

         # for 2D arrays save the row and columns into a var
        Row = len(matrix)
        Col = len(matrix[0])

        # flip matrix
        start = 0
        end = Row - 1
        while(end > start):
            for i in range(0,Col):
                #print("swapping " + str(matrix[start][i]) + " with " + str(matrix[end][i]))
                matrix[start][i], matrix[end][i] =  matrix[end][i], matrix[start][i]
            start += 1
            end -= 1

        # flip over horizontal axis
        start = 0
        end = 0
        for i in range(0,Row):
            for k in range(i,Col):
                if(end == start):
                    pass
                else:
                    temp = matrix[i][start]
                    matrix[i][start] = matrix[k][end]
                    matrix[k][end] = temp
                   # matrix[i][start], matrix[k][end] =  matrix[i][start], matrix[k][end]
                start += 1
            end += 1
            start = end

       # printout matrix
        # for i in range(0,len(matrix)):
        #     for j in range(0, len(matrix)):
        #         print(matrix[i][j], end=" ")
        #     print()


        

        # Second try: Use Numpy array for better time and space complexity
        # question won't let you create a new array even if its numpy

        # import numpy as np
        # npMatrix = np.array(matrix)

        # npMatrix = np.rot90(npMatrix, k=1, axes=(1, 0))

        # matrix = npMatrix

        # matrix = matrix.tolist()
