# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first attempt: very similar to cycle finding, we just need to return the node
        # we will use a runner to check for cycles and when the runner hits the slow pointer 
        # we return that node
        # we need the index of the start of the cycle, using the cycle finder just tells us if there 
        # is a cycle.
        # instead we could make a set or dictionary and see if the node is in the set or not and if it already is then we 
        # found the start of our cycle
        

        seenSoFar = {}
        seenSoFar[head] = 1

        while head != None and head.next != None:
            head = head.next
            if head in seenSoFar:       # using "in" has n runtime
                return head
            else:
                seenSoFar[head] = 1
        return None