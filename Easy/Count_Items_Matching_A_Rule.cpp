/*
Prompt: 
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are 
also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule. 

Example:
Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
*/


class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int itemsFollow = 0;
        unsigned char rule = 0; //assume ruleKey == "type"
        
        
        if(ruleKey == "color"){
           rule = 1;
        }
        else if(ruleKey == "name"){
           rule = 2;
        }
        
         for(int i = 0; i < items.size(); i++){
            if(ruleValue == items.at(i).at(rule)){
                itemsFollow++;
            }
        }
        
        return itemsFollow;
    }
};


/*
Notes:
Might be faster/less memory to use switch case statements but they aren't very friendly with strings.
instead of writing the for loop three times for each case we can just change the number in the if statement

Constraints:
1 <= items.length <= 104
1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
ruleKey is equal to either "type", "color", or "name".

*/
