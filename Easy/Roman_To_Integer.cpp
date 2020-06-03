#include <stdio.h>

//parse the string
//I = 1, V = 5, X = 10 and so on
//then add it all up
//doesnt check for incorrect roman numerals ordering
class Solution {
public:
    int romanToInt(string s) {
        int Total = 0;
        int next = 0;
        int curr = 0;
        for(int i = 0; i < s.size(); i++){
            curr = convertRomanToNum(s.at(i));
            if( i+1 != s.size()){
                next = convertRomanToNum(s.at(i+1));
            }
            else{
                next = 0;
            }
            if(next > curr){    //subtracting
                Total += (next - curr);
                i++;
            }
            else{
                Total += curr;
            }   
            //cout << "Total = " << Total << "\n";
        }
        return Total;
    }
    
    int convertRomanToNum(char c){
        if(c == 'I'){
            return 1;
        }
        else if(c == 'V'){
            return 5;
        }
        else if(c == 'X'){
            return 10;
        }
        else if(c == 'L'){
            return 50;
        }
        else if(c == 'C'){
            return 100;
        }
        else if(c == 'D'){
            return 500;
        }
        else{
            return 1000;
        }
    }
};