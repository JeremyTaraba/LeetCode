/*
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.



*/



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
Since there are no repeat numbers we could sort through once and find all mins in each row and all 
max in each column and see if any are the same. This should reduce runtime and space
This would require one O(N^2) loop to find mins and maxes and another O(N) loop to find 
which numbers are the same



Constraints:
m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.


*/