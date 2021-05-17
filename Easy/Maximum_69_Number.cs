/*
Prompt:
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

*/

public class Solution {
    public int Maximum69Number (int num) {
        String numberString = num.ToString();
        StringBuilder sb = new StringBuilder(numberString);
 
        for (int i = 0; i < numberString.Length; i++){       
            if(sb[i] == '6'){
                sb[i] = '9';
                break;
            }
            
        }
        numberString = sb.ToString();
       
        int result = Int32.Parse(numberString);
        return result;
    }
}

/*
Notes:
O(n) time to loop through every digit of the int

Constraints:
1 <= num <= 10^4
num's digits are 6 or 9.

*/