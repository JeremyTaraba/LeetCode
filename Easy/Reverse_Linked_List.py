# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # First attempt: iterate through the linked list and add each element to a list, could also do a stack to be easier
    # then go through that list in reverse order or go through the stack popping each element and adding them to a new ListNode instance
    # runtime of O(n) and space of O(n) for the list/stack
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        tempList = []
        while head:
            tempList.append(head.val)
            head = head.next

        newHead = ListNode(tempList[len(tempList)-1])
        tempHead = newHead
        for num in tempList[::-1][1:]:
            temp = ListNode(num)
            tempHead.next = temp
            tempHead = tempHead.next
        
        return newHead

        
        