/*
Prompt:
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

*/


class Solution {
    
    public static int FindIndex(int[] nums, int beg, int end, int target){
        if(beg <= end){
            int mid = beg + (end - beg)/2;
            if(nums[mid] == target){
                return mid;
            }
            if(nums[mid] > target){
                return FindIndex(nums, beg, mid-1, target);
            }
            return FindIndex(nums, mid+1, end, target);
        }
        return -1;
    }
    
    
    
    public int search(int[] nums, int target) {     
        
        return FindIndex(nums, 0, nums.length-1, target);
    }
}

/*
Notes:
Simple binary search algorithm. Tried to make it a while loop instead of 
its own functions but  its not as optimal.

Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.


*/