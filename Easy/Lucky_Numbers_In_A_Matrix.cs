public class Solution {
    public IList<int> LuckyNumbers (int[][] matrix) {
        int rowLength = matrix.Length;
        int columnLength = matrix[0].Length;
        List<int> numbers = new List<int>();
        
        int min;
        int minIndex;
        int max;
        int maxIndex;
        for(int i = 0; i < rowLength; i++){
            minIndex = 0;
            maxIndex = 0;
            min = matrix[i][0];
            for(int j = 0; j < columnLength; j++){
                if(min > matrix[i][j]){
                    min = matrix[i][j];
                    minIndex = j;
                }
            }
            max = matrix[0][minIndex];
            for(int k = 0; k < rowLength; k++){
                if(max < matrix[k][minIndex]){
                    max = matrix[k][minIndex];
                    maxIndex = k;
                }
            }
            
            if(matrix[i][minIndex] == matrix[maxIndex][minIndex]){
                numbers.Add(min);
            }
        }
        
        return numbers;
    }
}

/*
Notes:



Constraints:
m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.


*/