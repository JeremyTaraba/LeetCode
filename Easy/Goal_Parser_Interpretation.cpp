/*
Prompt:
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings 
are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.


Example:
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".


*/




#include <string>

class Solution {
public:
    string interpret(string command) {
        string goal;
        for(int i = 0; i < command.size(); i++){
            if(command.at(i) == 'G'){
                goal.append("G");
            }
            else if(command.at(i) == '('){
                if(command.at(i+1) == ')'){
                    goal.append("o");
                    i++;
                }
                else if(command.at(i+1) == 'a'){
                    goal.append("al");
                    i+=3;
                }
            }
        }
        return goal;
    }
};

/*
Notes:
Instead of making a new string and appending to it we could also just manipulate the input string directly and return it. Would save space that way.



Constraints:
1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.

*/