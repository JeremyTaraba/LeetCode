/*
Prompt:
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

*/


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
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


*/