from collections import deque


def binarySearch(list, target):
    right = len(list)
    left = 0
    ans = False
    while(right >= left):
        mid = left + (right - left) // 2
        if(list[mid] == target):
            ans = True
            break
        if(list[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    print(ans)



class node:
    
    def __init__(self, value, right, left) -> None:
        self.value = value
        self.left= left
        self.right = right


root = node(1, None, None)
node2 = node(2, None, None)
node3 = node(3, None, None)
node4 = node(4, None, None)
node5 = node(5, None, None) 

root.left = node2
root.right = node3
node2.left = node4
node3.right = node5

list = [1,2,3,4,5,6,7,8,9,10]

binarySearch(list, 3)