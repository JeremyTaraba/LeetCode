# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
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

        
        