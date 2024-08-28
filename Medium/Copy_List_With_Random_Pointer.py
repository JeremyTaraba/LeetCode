"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # go through list until there no more next
        if not head:
            return

        # create hashmap to store nodes
        hashMap = { None: None}


        # works but doesnt take random into account
        cur = head
        while cur:
            tempNode = Node(cur.val)
            hashMap[cur] = tempNode
            cur = cur.next


        cur = head
        while cur:
            tempNode = hashMap[cur]
            tempNode.next = hashMap[cur.next]
            tempNode.random = hashMap[cur.random]
            cur = cur.next



        return hashMap[head]
