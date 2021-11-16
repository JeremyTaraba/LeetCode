/*
Prompt:
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


*/


class Solution {
    
    public static int FindIndex(int[] nums, int beg, int end, int target){
        if(target >= nums[beg]){
            int mid = beg + (end - beg)/2;
            if(nums[mid] == target){
                return mid;
            }
            if(nums[mid] < target && nums[mid+1] > target){
                return mid+1;
            }
            if(nums[mid] > target){
                return FindIndex(nums, beg, mid-1, target);
            }
            return FindIndex(nums, mid+1, end, target);
        }
        return -1;
    }
    
    
    public int searchInsert(int[] nums, int target) {
        if(nums.length == 1){
            if(target <= nums[0]){
                return 0;
            }
            return 1;
        }
        
        int firstNum = nums[0];
        int lastNum = nums[nums.length - 1];
        if(firstNum > target){
            return 0;
        }
        if(lastNum < target){
            return nums.length;
        }
        
        return FindIndex(nums, 0, nums.length-1, target);
       
        
        
        
    }
}

/*
Notes:
This solutions is similar to finding the index of an item if it existed although
for this problem the target number may not actually exist.
I used a binary search algorithm and modified it so it worked if the number 
didn't exist.


Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104


*/