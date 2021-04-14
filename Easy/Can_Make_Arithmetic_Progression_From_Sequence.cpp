/*
Prompt:
Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.


 
*/




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

/*
Notes:
we have to sort the vector first.


Constraints:
2 <= arr.length <= 1000
-10^6 <= arr[i] <= 10^6

*/