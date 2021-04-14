
#include <algorithm>    // std::sort

class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int lastNum = arr.at(0) - arr.at(1);
        for(int i = 0; i < arr.size()-1; i++){
            if(arr.at(i) - arr.at(i+1) != lastNum){
                return false;
            }
        }
        return true;
    }
};