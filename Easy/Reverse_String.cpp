class Solution {
public:
    void reverseString(vector<char>& s) {
        for (int i = 0, j = s.size()-1; i < j; i++, j--) {
            swap(s[i], s[j]);
        }
    }
};

/*
Notes:
Compared to python or c# this method is much faster and even using the built in algorithm for reversing a vector is slower 
than just swapping both ends


Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.


*/