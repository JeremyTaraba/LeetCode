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

/*
Notes:
This way preserves the original array but moves the unwanted numbers to the back, the alternative is to just overrite the unwanted numbers


Constraint:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

*/