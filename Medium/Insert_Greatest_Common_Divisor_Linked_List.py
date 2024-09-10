# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # make a function for find divisor, O(min(a,b))
        # save those in a list
        # go through the linked list again and insert them O(n) runtime and O(n) space

        def gcd(a, b):

            # Find minimum of a and b
            result = min(a, b)

            while result:
                if a % result == 0 and b % result == 0:
                    break
                result -= 1

            # Return the gcd of a and b
            return result

        ans = []
        headPntr = head

        while headPntr.next:
            a = headPntr.val
            b = headPntr.next.val
            divisor = gcd(a,b)
            temp = ListNode(divisor)
            temp.next = headPntr.next
            headPntr.next = temp
            # ans.append(divisor)   # we can ignore the array and just add the values as we see them, same runtime but less code
            headPntr = headPntr.next.next
        
        # headPntr = head
        # for val in ans:
        #     temp = ListNode(val)
        #     temp.next = headPntr.next
        #     headPntr.next = temp
        #     headPntr = headPntr.next.next


        return head

        