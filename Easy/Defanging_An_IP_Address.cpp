#include <string>

class Solution {
public:
    string defangIPaddr(string address) {
        string defang = "";
        for(int i = 0; i < address.size(); i++){
            if(address.at(i) == '.'){
                defang.append("[.]");
            }
            else{
                defang.append(address, i, 1);   //append address at index i for 1 character
            }
        }
        
        return defang;
    }
};