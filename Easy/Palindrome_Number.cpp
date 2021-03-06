#include <iostream>
#include <string>
using namespace std;

//NOTE: this does not work for decimals since we are using an int
//We can implement isdigit to check each character of the input to see if input is actually a number
//we can change the number to be a float to include decimals.

class Solution {
public:
    bool isPalindrome(int x) {
        
        if((x < 0) || (x % 10 == 0 && x != 0)){
            return false;
        };
        bool r = true;
        string s = to_string(x);
        int l = s.size() - 1;
        for(int i = 0; i < s.size() / 2; i++){
            if(s.at(i) != s.at(l)){
                r = false;
                break;
            }
            l = l - 1;
        }
        return r;
    }
};

int main(){
    Solution palindrome;
    int num;

    cout << "Enter number to be checked if it is a Palindrome" << endl;

    if (!(cin >> num)){             //this only checks if input starts with a character. otherwise ignores characters
        cout << "You did not enter a valid number" << endl;
        return 0;
    }
    
    if( palindrome.isPalindrome(num) ){
        cout << "Yes, You entered a Palindrome" << endl;
    }
    else{
        cout << "No, The number you entered is NOT a Palindrome" << endl;
    } 

    return 0;
}