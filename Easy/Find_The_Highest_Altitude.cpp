class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int highest = 0;
        short int sum = 0;
        for(int i = 0; i < gain.size(); i++){
            sum += gain.at(i);
            if(sum > highest){
                highest = sum;
            }
        }
        
        return highest;
    }
};

/*
Notes:
O(n) time complexity 
order of the vector matters so we can rearrange it.


Constraints:
n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100


*/