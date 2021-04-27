public class Solution {
    public bool IsPalindrome(string s) {
        string alphanumeric = s.ToLower();  //make letters lowercase
        
        var sb = new StringBuilder();

        foreach (char c in alphanumeric)
        {
           if ( (c >= '0' && c <= '9') || (c >= 'a' && c <= 'z') ){     //accepts only letters or numbers
              sb.Append(c);
           }
        }

        alphanumeric = sb.ToString();
        Console.WriteLine(alphanumeric);       //check to make sure not characters got in
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

/*
Notes:



Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters


*/