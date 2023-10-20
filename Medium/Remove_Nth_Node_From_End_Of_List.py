# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first attempt: to remove this node we need to count how far we are from the tail and then go back to the nth node
        # for linkedList problems we can generally use recursion or a runner pointer and current pointer (2 indices)

        current = head
        runner = head

        for i in range(n):
            runner = runner.next
        
        if not runner:  # if n = length of linkedlist
            return head.next
        
        while runner.next:
            current = current.next
            runner = runner.next
        
        current.next = current.next.next

        return head
        