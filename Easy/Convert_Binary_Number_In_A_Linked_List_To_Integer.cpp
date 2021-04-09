/*
Prompt:
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Ex:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
*/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    int getDecimalValue(ListNode* head) {
        int decimal = 0;
        
        while(head != NULL){
            if(head->val == 1){     //left shift decimal. Ex: decimal = 101 then left shift, decimal = 1010. Then add 1 so decimal = 1011
                decimal = (decimal << 1);
                decimal++;
            }
            else{   //left shift decimal. Ex: decimal = 101 then left shift, decimal = 1010
                decimal = (decimal << 1);
            }
            head = head->next;
        }
        
        return decimal;
    }
};


/*
Notes:
complexity is O(n), can't reduce this any further.


Constraints:
The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
*/