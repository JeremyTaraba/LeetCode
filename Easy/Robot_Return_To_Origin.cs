public class Solution {
    public bool JudgeCircle(string moves) {
        int LRCounter = 0;
        int UDCounter = 0;

        for(int i = 0; i < moves.Length; i++){
            if(moves[i] == 'U'){
                UDCounter++;
            }
            else if(moves[i] == 'D'){
                UDCounter--;
            }
            else if(moves[i] == 'R'){
                LRCounter++;
            }
            else if(moves[i] == 'L'){
                LRCounter--;
            }
        }
        
        return LRCounter == 0 && UDCounter == 0;
    }
}

/*
Notes:
Switch case might be more efficient
We could also use only one int as a counter instead of two, just add different numbers for LR and UD
Example:
LR we add or subtract two but for UD we add or subtract seven and at the end we see if the int equals 0 or not.
The problem with this is that there is the case where we add 7 nine times and subtract 9 seven times, in which case we would not be at the origin
but the int would equal zero.


Constraints:
1 <= moves.length <= 2 * 104
moves only contains the characters 'U', 'D', 'L' and 'R'.

*/