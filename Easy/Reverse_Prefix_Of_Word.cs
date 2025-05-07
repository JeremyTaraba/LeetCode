public class Solution {
    public string ReversePrefix(string word, char ch) {
        int index = word.IndexOf(ch);
        if(index != -1){
            char[] subString = word.Substring(0,index+1).ToCharArray();
            
            Array.Reverse(subString);
            return new string(subString) + word.Substring(index+1);
        }
        return word;
    }
}