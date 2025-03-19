public class Solution {
    public int MinOperations(int[] nums) {
        // odd number and even numbers will be different
        // [0,1,1,1,0] = [1,0,0,1,0] = [1,1,1,0,0] = [1,1,0,1,1] impossible
        // last 2 elements must be 1's for it to be possible
        int size = nums.Length;
        int res = 0;

        for (int i = 0; i < size-2; i++){
            if(nums[i] == 0){
                nums[i+1] ^= 1;
                nums[i+2] ^= 1;
                res += 1;
            }
        }
        


        if(nums[size-1] == 1 && nums[size-2] == 1){
            return res;
        }
        else{
            return -1;
        }
    }
}