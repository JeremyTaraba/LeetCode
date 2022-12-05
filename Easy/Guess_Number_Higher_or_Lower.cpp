/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */
 
class Solution {       
public: 
    int guessNumber(int n) {
        unsigned guessNum = n/2;
        unsigned lowerBound = 1;
        unsigned higherBound = n;
        int checkGuess = guess(guessNum);     
        
        while(checkGuess != 0){
            if(checkGuess == 1){ 
                lowerBound = guessNum + 1;
                guessNum = (lowerBound + higherBound)/2;
            }
            if(checkGuess == -1){
                higherBound = guessNum - 1;
                guessNum = (lowerBound + higherBound)/2;
            }
            checkGuess = guess(guessNum);
        }
        return guessNum;
    }
};