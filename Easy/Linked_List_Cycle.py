# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # First attempt: assuming the list is in no particular order. The only way to tell
        # if the list cycles is by checking the memory adress and seeing if you have seen it before
        # could make a dictionary or set and check for duplicate adress
        # alternatively could use Floyd's cycle finding algorithm which has the same
        # time complexity as set or dictionary but an O(1) space complexity.


         # Floyd's Cycle Finding Algorithm

        first = head # faster 1
        second = head # slower 1

        while(second != None and first != None and first.next != None):    
            first = first.next.next
            second = second.next

            if(first == second):
                return True
        return False