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
        
        if not head:
            return None
        

        # seenSoFar = {}
        # seenSoFar[head] = 1

        # while head != None and head.next != None:
        #     head = head.next
        #     if head in seenSoFar:       # using "in" has n runtime
        #         return head
        #     else:
        #         seenSoFar[head] = 1
        # return None



        # second attempt: to solve this in O(1) memory we can either modify the data when we see it but the 
        # question tells us not to do that
        # so we can instead use a runner. If those pointers meet then we know we have a cycle like in cycle finding but 
        # to get the start of the cycle we then move the slow pointer back to the head and move both pointers by 1 and see 
        # where they meet. That will be the start of the cycle. The reason this works is because of math

        curr = head
        runner = head

        while runner.next and runner.next.next:
            curr = curr.next
            runner = runner.next.next
            if curr == runner:
                curr = head
                while curr != runner:
                    curr = curr.next
                    runner = runner.next
                return curr
        return None
        



