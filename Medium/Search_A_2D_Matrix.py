class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first attempt: searching for number in sorted list so cut list and half and 
        # search and keep cutting in half. What if we find correct row first? and then 
        # go through that row with the half algorithm


        Rows = len(matrix)-1
        Col = len(matrix[0])-1

        if(matrix[Rows][Col] < target):
                return False

        # find correct row in O(m) time
        correctRow = -1
        lessThan = False
        while(correctRow == -1):
            if(matrix[Rows][Col] < target):
                correctRow = Rows+1
            else:
                Rows-=1
                if(Rows == -1):     # target is less than first rows last number
                    correctRow = Rows+1
            
        # search row in O(n) time
       
        for i in matrix[correctRow]:
            if(i == target):
                return True

        return False
