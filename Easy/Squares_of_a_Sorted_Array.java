/*
Prompt:
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


*/



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

/*
Notes:
We have two different pointers, one to where the positive integers start and one from where the 
negative integers start. For the positive we will increment it each time we square and add that
number and for the negative pointer we will decrement it. this goes on until we reach the end
for either one end then we finish the other pointer. 


Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

*/