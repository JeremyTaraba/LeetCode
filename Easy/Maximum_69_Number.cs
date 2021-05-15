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