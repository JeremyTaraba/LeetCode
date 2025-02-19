public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        // first find the row, then find the value in that row. Use binary search for both
        int rowSize = matrix.Length;
        int colSize = matrix[0].Length;
        

        // find the targetRow first
        int targetRow = -1;
        int top = 0;
        int bottom = rowSize-1;
        int mid = 0;
        while (top <= bottom){
            mid = top + (bottom - top) / 2;
            int leftVal = matrix[mid][0];
            int rightVal = matrix[mid][colSize-1];
            

            if (target == leftVal || target == rightVal){
                return true;
            }
            if (target > leftVal && target < rightVal){
                targetRow = mid;
                break;
            }
            if (target < leftVal){
                bottom = mid-1;
            }
            else if (target > rightVal){
                top = mid+1;
            }

        }
        if(targetRow == -1){
            return false;
        }

        // find the target in the row
        int left = 0;
        int right = colSize-1;
        Console.WriteLine(targetRow);
        while(left <= right){
            mid = left + (right - left) / 2;
            if(matrix[targetRow][mid] == target){
                return true;
            }
            else if(target < matrix[targetRow][mid]){
                right = mid-1;
            }
            else{
                left = mid+1;
            }
        }




        return false;

    }
}