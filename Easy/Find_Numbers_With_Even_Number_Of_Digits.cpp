//the size of the number doesn't matter
//all we do is subtract one digit from the number
//and keep track of how many digits we subtracted
//do this for each one

class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int temp;
        int counter;
        int evenDigCount = 0;
        for( int i = 0; i < nums.size(); i++){
            temp = nums.at(i);
            counter = 1;
            while( temp > 9 ){       //while the number has more than 1 digit in it
                counter++;          //keep track of even or odd
                temp = temp / 10;
            }
            if(counter % 2 == 0){
                evenDigCount++;
            }
        }
        return evenDigCount;
    }
};