#include <string>
class Solution {
public:
    string toLowerCase(string str) {
        string lowerCase = "";
        for(int i = 0; i < str.size(); i++){
            if(str.at(i) >= 65 && str.at(i) <= 90){
                lowerCase += (str.at(i) + 32);
            }
            else{
                lowerCase += (str.at(i));
            }
        }
        return lowerCase;
    }
};