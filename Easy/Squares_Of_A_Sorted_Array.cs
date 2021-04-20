public class Solution {
    public int[] SortedSquares(int[] nums) {
        for(int i = 0; i < nums.Length; i++){
            nums[i] = nums[i] * nums[i];
        }
        Array.Sort(nums);
        return nums;
    }
}

/*
Notes:
Another way to do it is to find the absolute value of the array first and then sort it and then square it
But that would take more steps.

Constraints:



*/