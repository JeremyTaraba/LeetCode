public class Solution {
    public string GcdOfStrings(string str1, string str2) {
        String res = "";

        String smaller = str2;
        String larger = str1;
        if(str1.Length < str2.Length){
            smaller = str1;
            larger = str2;
        }

        // find largest common denominator to determine largest possible string
        int LCD = 1;
        for(int i = 1; i < smaller.Length+1; i++){
            if(smaller.Length % i == 0 && larger.Length % i == 0){
                LCD = i;
            }   
        }
       
        int count = 0;
        int smallerCount = 0;
        for(int i = 0; i < larger.Length; i++){
            smallerCount = i % smaller.Length;
            if(smaller[smallerCount] == larger[i]){
                if(count < LCD){
                    count++;
                }
            }
            else{
                return "";
            }
        }
        res = smaller.Substring(0,count);
        for (int i = 0; i < smaller.Length; i++){
            if(smaller[i] != res[i % res.Length]){
                return "";
            }
        }



        return res;
    }
}