# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        
        cur = head
        root = cur
        run = head.next
        cur.next = run.next
        run.next = cur
        root = run
        cur, run = run, cur
        while run.next and run.next.next:
            prev = run
            cur = run.next
            run = cur.next
            cur.next = run.next
            run.next = cur
            prev.next = run
            cur, run = run, cur
        
        return root