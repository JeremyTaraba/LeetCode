# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # First attempt: Go through the list linearly and remove target values O(n) runtime

        if(head == None):
            return head
        while(head.val == val):
            if(head.next == None):
                return head.next
            head = head.next

        if(head.next == None):
            return head
        temp = head
        front = head.next

        while(front != None):
            if(front.val == val):
                while(front.val == val):
                    if(front.next == None):
                        temp.next = None
                        return head
                    front = front.next
                temp.next = front
            temp = temp.next
            front = temp.next
            
            
        return head


   

