# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # save all values to a list and then go through that list when adding to head O(n) runtime and space
        # when going through the list use 2 pointers so your at correct index
        # technically only need the last half of the linkedlist and can append every other node instead of recreating the Linked List

        copy = []
        headPntr = head
        headPntr = headPntr.next # don't need first val
        while headPntr:
            copy.append(headPntr.val)
            headPntr = headPntr.next

        l = 0
        r = len(copy) - 1
        flip = True
        while r >= l:
            if flip:
                temp = ListNode(copy[r])
                r -= 1
            else:
                temp = ListNode(copy[l])
                l += 1
            flip = not flip
            head.next = temp
            head = head.next

