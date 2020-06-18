#include <iostream>
#include <string>

using namespace std;
const int MAX_CHAR = 26;

class Solution {
public:
    string sortString(string s) {
      
        //sort string s
        string sorted = "";
        int charCount[MAX_CHAR] = {0}; 

        for (int i = 0; i < s.length(); i++){ 
            charCount[s[i]-'a']++;     
        }
        for (int i = 0;i < MAX_CHAR; i++){
            for (int j=0;j<charCount[i];j++) {
                sorted += 'a'+i; 
            }
        }
        // https://www.geeksforgeeks.org/sort-string-characters/
        
        string result = "";
        char last_char;
        bool all_tilda = false;
        
        while(!all_tilda){
            //set last char for smallest
            for(int i = 0; i < sorted.length(); i++){
                if(sorted.at(i) != '~'){
                    last_char = sorted.at(i);
                    result+= sorted.at(i);
                    sorted.replace(i,1,"~");
                    break;
                }
            }
            for(int i = 0; i < sorted.length(); i++){
                if(sorted.at(i) != '~'){
                    if(last_char < sorted.at(i)){  
                        result += sorted.at(i);
                        last_char = sorted.at(i);
                        sorted.replace(i,1,"~");
                    }
                }

            }   
            //set last char for largest
            for(int i = sorted.length()-1; i >= 0; i-- ){
                if(sorted.at(i) != '~'){
                    last_char = sorted.at(i);
                    result+=sorted.at(i);
                    sorted.replace(i,1,"~");
                    break;
                }
            }
            for(int i = sorted.length()-1; i >= 0; i--){
                if(sorted.at(i) != '~'){
                    if(sorted.at(i) < last_char){
                        result += sorted.at(i);
                        last_char = sorted.at(i);
                        sorted.replace(i,1,"~");
                    }

                }
            }
            for(int i = 0; i < sorted.length(); i++){
                if(sorted.at(i) == '~'){
                    all_tilda = true;
                }
                else{
                    all_tilda = false;
                    break;
                }
            }
        }
        
        return result;
    }
};