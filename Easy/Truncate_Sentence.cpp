class Solution {
public:
    string truncateSentence(string s, int k) {
        string sentence;
        int numSpaces = 0;
        int lastIndex = 0;
        int i;
        for(i = 0; i < s.size(); i++){
            if(numSpaces >= k){
                break;
            }
            if(s.at(i) == ' '){
                numSpaces++;
                sentence.append(s, lastIndex, i-lastIndex);
                lastIndex = i;
            }
        }
        
        if(i == s.size()){  //went through the loop and every space is allowed then sentence will be the same as s
            sentence = s;
        }
        
        return sentence;
    }
};

/*
Notes:


Constraints:
1 <= s.length <= 500
k is in the range [1, the number of words in s].
s consist of only lowercase and uppercase English letters and spaces.
The words in s are separated by a single space.
There are no leading or trailing spaces.


*/