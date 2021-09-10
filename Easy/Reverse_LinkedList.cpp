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

#include <bits/stdc++.h>
#include <iostream>
#include <stack>
using namespace std;

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == NULL){
            return 0;
        }
        
        stack<ListNode*> s;
        ListNode* node = head;
        
        
        while(node->next != NULL){
            s.push(node);
            node = node->next;
        }
        
        ListNode* ans = node;
        
        while(!s.empty()){
            node->next = s.top();
            s.pop();
            node = node->next;
        }
        node->next = NULL;
    
    
        return ans;
    }
}; 
 
/*
Notes:
could also use recursion for less memory usage

*/