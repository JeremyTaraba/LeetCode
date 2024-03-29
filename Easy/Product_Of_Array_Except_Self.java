import java.util.Arrays;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        // multiple all nums together and divide by itself
        // O(1) space and O(n) runtime

        int product = 1;
        boolean zero = false;
        int indexOfZero = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 0){
                if(zero){
                    Arrays.fill(nums,0);
                    return nums;
                }
                else{
                    zero = true;
                    indexOfZero = i;
                }
            }
            else{
                product *= nums[i];
            }   
        }
        if(zero){
            Arrays.fill(nums,0);
            nums[indexOfZero] = product;
        }
        else{
            for(int i = 0; i < nums.length; i++){
                nums[i] = product / nums[i];
            }
        }


        
        return nums;

    }
}