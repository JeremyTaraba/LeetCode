public class Solution {
    public bool IsPalindrome(string s) {
        string alphanumeric = s.ToLower();
        
        var sb = new StringBuilder();

        foreach (char c in alphanumeric)
        {
           if ( (c >= '0' && c <= '9') || (c >= 'a' && c <= 'z') ){
              sb.Append(c);
           }
        }

        alphanumeric = sb.ToString();
        Console.WriteLine(alphanumeric);
        int backCounter = alphanumeric.Length - 1;
        
        for(int i = 0; i < alphanumeric.Length/2; i++){
            if(alphanumeric[i] != alphanumeric[backCounter]){
                return false;
            }
            backCounter--;
        }
        
        return true;
    }
}