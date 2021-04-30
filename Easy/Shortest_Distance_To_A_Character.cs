public class Solution {
    public int[] ShortestToChar(string s, char c) {
        int[] answer = new int[s.Length];
        int count = -1;    
        bool firstCharacter = false;
        
        /*
        Forward Fill loop
        First loop is used to correctly output all distances after the first char c is found.
        We treat everything before that first c as unknown until we find a c and now we can count up from that e
        the problem now is, when we run into another c we counted up then hit distance 0
        ex: -1 -1 -1 0 1 2 3 4 0 
        where each 0 is a c. To fix this we do another loop starting from the back
        */
        for(int i = 0; i < s.Length; i++){
            if(s[i] == c){
                count = 0;
                firstCharacter = true;
            }
			else if(firstCharacter){
                count++;
            }
            
            answer[i] = count;
            /*foreach(var item in answer){
                Console.Write(item.ToString());
            }
            Console.Write('\n');*/
        }
        
        /*
        BackWard fill loop
        Second loop starts from the back and corrects what the first loop could not get. 
        ex: -1 -1 -1 0 1 2 3 4 0 turns into -1 -1 -1 0 1 2 3 1 0 after the first pass
        We don't need to use bool firstCharacter for this one
        */
         for(int i = s.Length-1; i >= 0; i--){
            if(s[i] == c){
                count = 0;
            }
			else {
                count++;
            }
             
             if(answer[i] == -1 || answer[i] > count){
                answer[i] = count;
			}
        }
        
        return answer;
    }
}