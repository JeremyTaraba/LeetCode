/*
Prompt:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

*/



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
This way preserves the original array but moves the unwanted numbers to the back, the alternative is to just overrite the unwanted numbers with the next wanted number
and push all the numbers down. 


Constraint:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

*/