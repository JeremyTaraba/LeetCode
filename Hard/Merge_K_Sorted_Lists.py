# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force in O(k*n) which would be going through all the lists for every value
        # can do this by having an array that saves which index we are on for each list
        # and looking for the min value of each list and creating a new list out of this.
        # could also merge 2 at a time then merge again until have 1 big list (merge sort) would be O(n * log k)

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergeList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergeList.append(self.mergeLists(l1,l2))
            lists = mergeList
        return lists[0]

        

    def mergeLists(self, l1, l2):
        temp = ListNode()
        pntr = temp
        while l1 and l2:
            if l1.val < l2.val:
                pntr.next = l1
                l1 = l1.next
            else:
                pntr.next = l2
                l2 = l2.next
            pntr = pntr.next
        if l1:
            pntr.next = l1
        if l2:
            pntr.next = l2
        return temp.next


