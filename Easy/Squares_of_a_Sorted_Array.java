



class Solution {
    public int[] sortedSquares(int[] nums) {
        int len = nums.length;
        int positiveIndex = 0;
        
        while(positiveIndex < len && nums[positiveIndex] < 0){
            positiveIndex++;    //find where the positives start
        }
        
        int negativeIndex = positiveIndex-1;
        int[] sortedSquares = new int[len];
        int counter = 0;    //keeps track of what index we are on
        
        while(negativeIndex >= 0 && positiveIndex < len){
            if(nums[positiveIndex] * nums[positiveIndex] < nums[negativeIndex] * nums[negativeIndex]){
                sortedSquares[counter] = nums[positiveIndex] * nums[positiveIndex];
                positiveIndex++;
            }
            else{
                sortedSquares[counter] = nums[negativeIndex] * nums[negativeIndex];
                negativeIndex--;
            }
            
            counter++;
        }
        //check edge cases incase there are more positive than negative numbers or vice versa
        
        while(negativeIndex >= 0){
            sortedSquares[counter] = nums[negativeIndex] * nums[negativeIndex];
            negativeIndex--;
            counter++;
        }
        while(positiveIndex < len){
            sortedSquares[counter] = nums[positiveIndex] * nums[positiveIndex];
            positiveIndex++;
            counter++;
        }
        
        
        
        return sortedSquares;
    }
}