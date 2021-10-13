class Solution {
    public int removeElement(int[] nums, int val) {
        if(nums.length == 0){
            return 0;
        }
        
        int curIndex = 0;
        for(int i = 1; i < nums.length; i++){
            if(nums[curIndex] == val){
                if(nums[i] != val){
                    int temp = nums[i];
                    nums[i] = nums[curIndex];
                    nums[curIndex] = temp;
                    curIndex++;
                }
            }
            else{
                curIndex++;
            }
        }
        
        if(nums[nums.length-1] != val){     //checks the last value since the loop doesn't check it
            return curIndex+1;
        }
        
        return curIndex;
    }
}