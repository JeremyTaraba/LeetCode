#include <vector>

class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> result;
        
        for(int i = 0; i < nums.size(); i=i+2){
            for(int k = 0; k < nums.at(i); k++){
                result.push_back(nums.at(i+1));
            }
        }
        
        
        return result;
    }
};