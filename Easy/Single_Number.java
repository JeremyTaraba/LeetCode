class Solution {
    public int singleNumber(int[] nums) {
        int answer = 0;

        for(int i = 0; i < nums.length; i++){
            answer = answer ^ nums[i]; //Bitwise XOR 
        }
        return answer;
    }
}

/*
Notes:
Using a bitwise XOR we can add the bits if we have never seen it and subtract the bits if we have seen them.
For example: 1, 3, 1. The answer should be 3
    001 ^ 010 = 011
    011 ^ 001 = 010
    010 = 3


Constraints:



*/