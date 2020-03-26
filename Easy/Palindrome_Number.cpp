#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        
        //lowered the memory and the runtime
        if((x < 0) || (x % 10 == 0 && x != 0)){
            return false;
        };
        bool r = true;
        string s = to_string(x);
        int l = s.size() - 1;
        for(int i = 0; i < s.size() / 2; i++){
            if(s.at(i) != s.at(l)){
                r = false;
                break;
            }
            l = l - 1;
        }
        return r;
    }
};