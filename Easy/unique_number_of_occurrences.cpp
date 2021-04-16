class Solution {
public:
    bool checkOccurrences(vector<int>& occur, int numOccur){
        for(int k = 0; k < occur.size(); k++){
                if(numOccur == occur.at(k)){
                    return false;   //occurs the same amount of time as something else
                }
            }
        return true;
    }
        
    bool uniqueOccurrences(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        arr.push_back(arr.at(arr.size()-1) + 1); //add a different value then the ending value
        vector<int> occurrences;
        int numOccur = 0;
        
        for(int i = 0; i < arr.size()-1; i++){
            if(arr.at(i) != arr.at(i+1)){
                numOccur++;
                if(!checkOccurrences(occurrences, numOccur)){
                    return false;
                }
                occurrences.push_back(numOccur);
                numOccur = 0;
            }
            else{
                numOccur++;
            }            
        }
        
        return true;
    }
};