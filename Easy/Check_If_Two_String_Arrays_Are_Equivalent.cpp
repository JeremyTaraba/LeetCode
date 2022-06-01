/*
Prompt:
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

  
*/  
class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string firstWord;
        string secondWord;
        for(short int i = 0; i < word1.size(); i++){
            firstWord.append(word1.at(i));
        }
        for(short int i = 0; i < word2.size(); i++){
            secondWord.append(word2.at(i));
        }
        if (firstWord.compare(secondWord) == 0){
            return true;
        }
        return false;
    }
};

/*
Notes:
All we do is take the vector and add it into one string then compare with the other vector.
Complexity should be O(n) for string.compare


Constraints:
1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.


*/