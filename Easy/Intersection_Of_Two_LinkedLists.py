# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # first attempt: if the lists are the same size we could just go down them at the same time and check if they 
        # equal each other. if A is bigger then we need to go down A until it is lined up with B and vice versa for B
        # to do this we would need the sizes of both lists, an O(n) operation in itself but O(1) space
        # Another approach is to go down list A and compare all value with the first value of B, then do this for the second
        # value and so on. This will take O(A*B) 
        # Lastly, we could use a hash table to store all nodes we have seen before and if we have a duplicate then thats 
        # the intersecting node. O(n) time but also O(n) space
        


        sizeA = 0
        sizeB = 0
        copyA = headA
        copyB = headB
        

        while copyA.next:
            copyA = copyA.next
            sizeA+=1

        while copyB.next:
            copyB = copyB.next
            sizeB+=1

        if copyA != copyB:      # check for intersection, last nodes should be the same if there is intersetion
            return None

        while sizeA > sizeB:
            headA = headA.next
            sizeA-=1
        while sizeB > sizeA:
            headB = headB.next
            sizeB-=1

        # sizes should be the same
        while headB != headA:
            headB = headB.next
            headA = headA.next

        return headA
            
        


