/*
Prompt:
A string is a valid parentheses string (denoted VPS) if it meets one of the following:

It is an empty string "", or a single character not equal to "(" or ")",
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s


*/

class Solution {
public:
    int maxDepth(string s) {
        signed char max = 0;
        signed char curDepth = 0;
        
        for(unsigned char i = 0; i < s.size(); i++){
            if(s.at(i) == '('){
                curDepth++;
                if(curDepth > max){
                    max = curDepth;
                }
            }
            if(s.at(i) == ')'){
                curDepth--;
                if(curDepth < 0){
                    return -1;  //error: not valid parenthesis
                }
            }
        }
        
        
        return max;
    }
};

/*
Notes:
Using signed chars instead of ints because the max size of string s is 100 so we save space.
The constraints say that string s is always a VPS but just incase we return -1 if it isn't


Constraints:
1 <= s.length <= 100
s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
It is guaranteed that parentheses expression s is a VPS.

*/