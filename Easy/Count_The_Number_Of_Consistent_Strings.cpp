/*
Prompt:
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Example:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

*/


class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int consistentStrings = 0;
        string temp;
        unsigned char erased = 0;
        for(unsigned char i = 0; i < allowed.size(); i++){
            for(int j = 0; j < words.size(); j++){
                temp = words.at(j);
                for(unsigned char k = 0; k < words.at(j).size(); k++){
                    if(allowed.at(i) == words.at(j).at(k)){
                        temp.erase(k - erased,1);
                        erased++;
                    }
                }
                words.at(j) = temp;
                erased = 0;
            }
        }
        
        for(int i = 0; i < words.size(); i++){
            if(words.at(i) == ""){
                consistentStrings++;
            }
        }
        
        return consistentStrings;
    }
};

/*
Notes:
When I go over each word, I erase any letters that are allowed. If the whole word is allowed then all letters will be erased and
the string will be empty.
There has to be a better way than using 3 for loops to do this. Or at least something faster than O(n^3)
A different coding language might be more efficient

Constraints:
1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.



*/