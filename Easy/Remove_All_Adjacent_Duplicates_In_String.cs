public class Solution {
    public string RemoveDuplicates(string S) {
        bool removeDup = true;
        
        while(removeDup){
            removeDup = false;
            for(int i = 0; i < S.Length-1; i++){
                if(S[i] == S[i+1]){
                    removeDup = true;
                    S = S.Remove(i, 2);
                    //Console.WriteLine(S);
                    break;
                }a
            } 
        }
        
        return S;
    }
}