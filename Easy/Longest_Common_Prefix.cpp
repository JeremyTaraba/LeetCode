class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int found = 0;
        string common = strs.at(0);     //assume first string is longest
        for(int i = strs.at(0).size()-1; i >= 0; i--){ //loop until we go through all letters
            for(int j = 1; j < strs.size(); j++){  //loop through all other strings
                size_t foundIndex = strs.at(j).find(common);
                if(foundIndex != string::npos && foundIndex == 0){ // we found it
                    found++;
                }
               
            }
            if(found == strs.size()-1){
                return common;
            }
            found = 0;
            common = common.substr(0,i);
        }
        return common;
    }
};