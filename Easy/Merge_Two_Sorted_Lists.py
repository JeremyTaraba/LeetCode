# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        newListHead = newList
        shorterList = 0


        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val >= list2.val:
            newList.val = list2.val
            list2 = list2.next
            shorterList = 2
            if not list2:
                newListHead.next = list1
                return newList
        else:
            newList.val = list1.val
            list1 = list1.next
            shorterList = 1
            if not list1:
                newListHead.next = list2
                return newList
            

        while list1 and list2:
            tempList = ListNode()
            if list1.val >= list2.val:
                tempList = list2
                newListHead.next = tempList
                newListHead = newListHead.next
                list2 = list2.next
                if not list2:
                    shorterList = 2
                    break
            else:
                tempList.val = list1.val
                newListHead.next = tempList
                newListHead = newListHead.next
                list1 = list1.next
                if not list1:
                    shorterList = 1
                    break
                
            
        if shorterList == 1:
            newListHead.next = list2
        else:
            newListHead.next = list1
           

        return newList
        