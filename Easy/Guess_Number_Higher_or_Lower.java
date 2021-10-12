/*
Prompt:
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.


*/

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

/*
Notes:
We constantly pick the middle number because it is the most efficient way to guess, especially when n becomes very large

Constraints:
1 <= n <= 231 - 1
1 <= pick <= n

*/