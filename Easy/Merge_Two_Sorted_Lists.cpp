/*
Prompt:
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == NULL){
            return l2;
        }
        if(l2 == NULL){
            return l1;
        }
        
        ListNode *root;
        if(l1->val <= l2->val){
            root = l1;
            root->next = mergeTwoLists(l1->next, l2);
        }
        else{
            root = l2;
            root->next = mergeTwoLists(l1, l2->next);
        }
        return root;
    }
};

/*
Notes:
This way uses recursion and is very fast. Another way to do this is to loop while boths lists have nodes
and in each loop iteration compare the current of one list with the current val of the other list

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

*/