#include <vector>

//try using quicksort on this
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> answer;
        int counter = 0;
        for(int i = 0; i < nums.size(); i++){
            counter = 0;
            for(int j = 0; j < nums.size();j++){
                if(nums.at(i) > nums.at(j)){
                    counter++;
                }
            }
            answer.push_back(counter);
        }
     
        
        return answer;
    }
};