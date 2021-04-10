/*
Prompt:
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).

For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.


*/


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