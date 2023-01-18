public class Solution {
    public bool IsIsomorphic(string s, string t) {
        // check if char is unique or not (have we seen it before)
        // if same answer for both then keep going but it not then stop

        int lenS = s.Length;
        int lenT = t.Length;

        if(lenS != lenT){
            return false;
        }

        bool uniqueS = true;
        bool uniqueT = true;
        Dictionary<char, char> letters = new Dictionary<char, char>();
        Dictionary<char, int> lettersT = new Dictionary<char, int>();

        for(int i = 0; i < lenS; i++){
            if(letters.ContainsKey(s[i])){
                uniqueS = false;
                if(t[i] != letters[s[i]]){
                    return false;
                }
            }
            else{
                letters.Add(s[i],t[i]);
                uniqueS = true;
            }
            if(lettersT.ContainsKey(t[i])){
                uniqueT = false;
            }
            else{
                lettersT.Add(t[i],1);
                uniqueT = true;
            }
            if(uniqueT != uniqueS){
                return false;
            }
        }

        return true;
    }
}