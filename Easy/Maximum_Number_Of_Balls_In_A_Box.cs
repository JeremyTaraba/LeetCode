public class Solution {
    public int CountBalls(int lowLimit, int highLimit) {
        int[] boxes = new int[46];    //arrays are initialized as 0's in c#
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

