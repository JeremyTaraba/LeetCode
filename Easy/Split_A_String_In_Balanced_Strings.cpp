//input strings can be any number of 'L' or 'R'

class Solution {
public:
    int balancedStringSplit(string s) {
        int stringCount = 0;
        int RLCount = 0;
        for(int i = 0; i < s.size(); i++){
            for(int j = i; j < s.size(); j++){
                if(s.at(j) == 'L'){
                    RLCount--;
                }
                else if(s.at(j) == 'R'){
                    RLCount++;
                }
                if(RLCount == 0){
                    i = j;
                    stringCount++;
                }
            }
            
        }
        return stringCount;
    }
};