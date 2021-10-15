class Solution {
    public int lengthOfLastWord(String s) {
        int length = 0;
        s = s.trim();
        for(int i = s.length()-1; i >= 0; i--){
            if(s.charAt(i) == ' '){
                return length;
            }
            length++;
        }
        
        return length;
    }
}

/*
Notes:
Another way to do this is to split() the string int a string[] array and get the length of the last element in that array.


Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.


*/