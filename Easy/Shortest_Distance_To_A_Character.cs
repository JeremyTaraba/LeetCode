/*
Prompt:
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

Example:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
 
*/


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

/*
Notes:
O(n) runtime

Constraints:
1 <= s.length <= 104
s[i] and c are lowercase English letters.
It is guaranteed that c occurs at least once in s.

*/