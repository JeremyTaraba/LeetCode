/*
Prompt:
You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.

Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.

Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.

 
Example:
Input: lowLimit = 1, highLimit = 10
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
Box 1 has the most number of balls with 2 balls.



*/



public class Solution {
    public int CountBalls(int lowLimit, int highLimit) {
        int[] boxes = new int[46];    //arrays are initialized as 0's in c#, Max number of boxes possible is 46
        int index = 0;
        for(int i = lowLimit; i <= highLimit; i++){
            int tempBox = 0;
            int tempi = i;
            while(tempi != 0){    
                tempBox += tempi % 10;
                
                tempi = tempi / 10;     //c# does not round up or down but returns a decimal
            }
            boxes[tempBox] = boxes[tempBox] + 1;
            index++;
        }
        
       
        return boxes.Max();
    }
}

/*
Notes:


Constraints:
1 <= lowLimit <= highLimit <= 105

*/
