# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # try using a stack
        if k == 1:
            return head

        stack = []
        cur = head
        prev = None
        top = None
        first = True
        while cur:
            if len(stack) >= k: # stack is full
                # reverse
                if prev:
                    prev.next = stack[-1]
                while len(stack) > 0:
                    # link all nodes inbetween
                    if top:
                        top.next = stack[-1]
                    top = stack.pop()
                    if first:
                        head = top
                        first = False
                top.next = cur
                prev = top
                top = None
            stack.append(cur)
            cur = cur.next

        # check if we have anything in the stack, if we do only reverse if the size == k
        # otherwise skip
        if len(stack) == k:
            # reverse
            if prev:
                prev.next = stack[-1]
            while len(stack) > 0:
                # link all nodes inbetween
                if top:
                    top.next = stack[-1]
                top = stack.pop()
                if first:
                    head = top
                    first = False
            top.next = cur
            prev = top
            top = None

        return head



