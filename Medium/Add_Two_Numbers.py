# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # first get the numbers 
        # then add them up
        # then put it back into a linked list
        # alternatively we could do this in place, we have to add them 1 digit at a time and carry over a 1 if needed
        # if one list is longer then we can use the shorter one as the base list

        # get size of lists to find shortest one
        size1 = 0
        size2 = 0

        l1Pointer = l1
        while l1Pointer:
            size1+=1
            l1Pointer = l1Pointer.next

        l2Pointer = l2
        while l2Pointer:
            size2+=1
            l2Pointer = l2Pointer.next

        main = l1
        shorter = l1
        longer = l2
        if size2 < size1:
            # l2 is shorter
            main = l2
            shorter = l2
            longer = l1
        
        carry = 0
        behind = shorter
        while shorter:
            shorter.val += carry
            carry = 0
            total = shorter.val + longer.val
            if total > 9:
                carry = 1
                total %= 10
            shorter.val = total
            behind = shorter
            shorter = shorter.next
            longer = longer.next

        if longer:
            behind.next = longer
        # finish longer
        while longer:
            total = longer.val + carry
            carry = 0
            if total > 9:
                carry = 1
                total %= 10
            print(total)
            behind.next.val = total
            behind = behind.next
            longer = longer.next
            
        
        # check carry
        if carry > 0:
            behind.next = ListNode(carry)






        return main


        
        