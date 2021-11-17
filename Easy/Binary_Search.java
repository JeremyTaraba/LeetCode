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