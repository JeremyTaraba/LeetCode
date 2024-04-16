class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // want to find correct row first then can binary search in row

        int rowIndex = 0;
        int columnIndex = 0;
        int rowSize = matrix.length;
        int columnSize = matrix[0].length;

        // binary search to find correct row
        int left = 0;
        int right = rowSize - 1;
        int mid = 0;
        while(left <= right){
            
            mid = left + (right - left) / 2;
            if(mid+1 > rowSize-1){
               rowIndex = rowSize-1;
               break; 
            }
            if(matrix[mid][0] <= target && matrix[mid+1][0] > target){
                rowIndex = mid;
                break;
            }
            else if(matrix[mid][0] < target){
                left = mid + 1;
            }
            else if(matrix[mid][0] > target){
                right = mid - 1;
            }
        }

        // binary search to find correct column
        left = 0;
        right = columnSize - 1;
        while(left <= right){
            
            mid = left + (right - left) / 2;
            
            if(matrix[rowIndex][mid] ==target){
                return true;
            }
            else if(matrix[rowIndex][mid] < target){
                left = mid + 1;
            }
            else if(matrix[rowIndex][mid] > target){
                right = mid - 1;
            }
        }

        



        return false;
    }
}