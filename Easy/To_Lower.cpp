#include <string>
  
//convert the given string into all lower case
//all we have to do is see if each character is in the ascii code for uppercase letters
//if yes then add 32 to change to lowercase letters
//32 is ascii difference between upper and lowercase

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