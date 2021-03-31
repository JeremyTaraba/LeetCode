/*
Prompt:
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.


*/



class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int equalPairs = 0;
        for(char i = 0; i < nums.size()-1; i++){
            for(char j = i+1; j < nums.size(); j++){
                if(nums.at(i) == nums.at(j)){
                    equalPairs++;
                }
            }
        }        
        return equalPairs;
    }
};

/*
Notes:
Sorting the vector first might make it faster

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100

*/