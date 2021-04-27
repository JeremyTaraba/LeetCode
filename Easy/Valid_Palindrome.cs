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
        
        for(int i = 0; i < alphanumeric.Length/2; i++){     //only need to go half of the string
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
Could use ToUpper instead of ToLower, shouldn't make much of a difference
Someone elses solution was to cut the string in half from the start and save each half in its own string and 
only accept letter or digits using IsLetterOrDigit(c). Then looped and commpared each side for as long as each side had charaters


Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters


*/