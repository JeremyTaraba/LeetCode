/*
Prompt:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


*/

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int lastSum = nums.at(0);
        vector<int> runningSum;
        runningSum.push_back(nums.at(0));
        short int vSize = nums.size();  //storing the size of the vector in datatype of short int to see if it saves space or time
        
        for(int i = 1; i < vSize; i++){
            runningSum.push_back(lastSum + nums.at(i));
            lastSum += nums.at(i);
        }
        
        return runningSum;
    }
};

/*
Can we reduce the run time to below O(n)?
Constraints: 
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

So highest possible value is if nums is size of 1000 and only has 10^6 as its value 
so lastSum would have 1,000,000,000 
int is the smallest datatype lastSum could be
*/