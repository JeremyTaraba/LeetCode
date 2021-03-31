/*
Prompt:
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.


*/



#include <string>

class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string shuffled = s;
        
        for(int i = 0; i < indices.size(); i++){
            shuffled.erase(indices.at(i), 1);
            shuffled.insert(indices.at(i), 1, s.at(i));
        }
        
        
        return shuffled;
    }
};

/*
Notes:
is there a way to lower the memory usage? like using string s instead of copying the contents of string s to string shuffled

Constraints:
s.length == indices.length == n
1 <= n <= 100
s contains only lower-case English letters.
0 <= indices[i] < n
All values of indices are unique (i.e. indices is a permutation of the integers from 0 to n - 1).


*/