/*
Prompt:
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

*/


class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> shuffled;
        short int evenCounter = 0;
        short int oddCounter = n;
        
        for(short int i = 0; i < nums.size(); i++){
            if(i % 2 == 0){  //i is an even number
                shuffled.push_back(nums.at(evenCounter));
                evenCounter++;
            }
            else{
                shuffled.push_back(nums.at(oddCounter));
                oddCounter++;
            }
        }
        
        return shuffled;
    }
};

/*
Notes:
using short ints instead of int for the variables lowers memory

Constraints:
1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3


*/