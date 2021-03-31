/*
Prompt:
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, 
which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.

*/


class ParkingSystem {
private:
    int psBig;
    int psMed;
    int psSmall;
    
public:
    ParkingSystem(int big, int medium, int small) {
        psBig = big;
        psMed = medium;
        psSmall = small;
    }
        
    bool addCar(int carType) {
        if(carType == 1){
            if(psBig > 0){
                psBig--;
                return true;
            }
        }
        else if(carType == 2){
            if(psMed > 0){
                psMed--;
                return true;
            }
        }
        else if(carType == 3){
            if(psSmall > 0){
                psSmall--;
                return true;
            }
        }
        return false;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */


/*
Notes:
Could use getter and setter functions but since addCar function is inside the class we might as well save time by not using them

Constraints:
0 <= big, medium, small <= 1000
carType is 1, 2, or 3
At most 1000 calls will be made to addCar


 */