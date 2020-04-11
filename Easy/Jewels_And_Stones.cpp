
//There is a faster way of doing this instead of a nested for loop

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int num_jewels = 0;
        for(int i = 0; i < J.size(); i++){
            for(int k = 0; k < S.size(); k++){
                if(J.at(i)== S.at(k)){
                    num_jewels++;
                }
            }
        }
        
        return num_jewels;
    }
};