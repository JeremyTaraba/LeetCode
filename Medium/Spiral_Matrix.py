class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 4 different directions to go
        direction = 1 # 1 -> left, 2 -> down, 3 -> right, 4 -> up

        r = 0
        c = 0
        ROW = len(matrix)
        COL = len(matrix[0])
        res = []
        loop = 0
        while len(res) != ROW*COL:
            res.append(matrix[r][c])
            if direction == 1:
                if c+1 == COL-loop:
                    direction+=1
                    r+=1
                    continue
                c+=1
            elif direction == 2:
                if r+1 == ROW-loop:
                    direction+=1
                    c-=1
                    continue
                r+=1
            elif direction == 3:
                if c-1 == -1+loop:
                    direction+=1
                    r-=1
                    loop+=1
                    continue
                c-=1
            else:
                if r-1 == -1+loop:
                    direction=1
                    c+=1
                    continue
                r-=1
                
        return res