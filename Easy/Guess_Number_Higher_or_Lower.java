/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

import java.lang.Math;


public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int numGuess = (int) Math.ceil( (double)n/2.0 );
        int highBound = n;
        int lowBound = 1;
        
        int guessResult = guess(numGuess);
        
        
        while(guessResult != 0){
            if(guessResult == -1){
                highBound = numGuess;
                numGuess = (highBound + lowBound ) / 2;
            }
            else{
                lowBound = numGuess;
                numGuess = (int) Math.ceil(( (double)highBound + (double)lowBound) / 2.0);
            }
            
            guessResult = guess(numGuess);
        }
        
        
        return numGuess;
    }
}