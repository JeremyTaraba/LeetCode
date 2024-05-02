import urllib.request, json


def compareTriplets(a, b):
    

    # Write your code here
    alice = 0
    bob = 0
    for i in range(0,len(a)):
        if(a[i] < b[i]):
            bob+=1
        elif(a[i] > b[i]):
            alice+=1
    print(alice)
    return [alice, bob]

def quicksort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot-1)
        quicksort(arr, pivot+1, right)

def partition(arr, left, right):
    pivotElement = arr[right]
    compareIndex = left-1

    for i in range(left, right):
        if arr[i] <= pivotElement:
            compareIndex +=1
            arr[compareIndex], arr[i] =  arr[i], arr[compareIndex]
    arr[compareIndex+1], arr[right] = arr[right], arr[compareIndex+1]
    return compareIndex+1

a = list(map(int, [1,2,3,5,10,9,1,4]))

b = list(map(int,  [0,2,3]))
#compareTriplets(a,b)



class BarGraph:
    

    def largestRectangleArea(self, heights) -> int:
            # find min, find area including min (by counting consecutive bars without 0), remove min.
            # ideal solution uses stack, maybe use stack to find consecutive bars

            myStack = []
            minNum = heights[0]
            myStack.append(minNum)
            maxHeight = 0


# need a find min function to find min value of next bar not at 0
            for i in range(1, len(heights)):

                counter = 1
                indexOfMin = 0
                while len(myStack) > 0 and counter < len(heights):
                    
                    if heights[counter] == 0:
                        height = self.findMaxHeight(myStack, minNum)
                        if(height > maxHeight):
                            maxHeight = height
                        myStack.clear()
                        if(counter+1 < len(heights)):
                            counter+=1
                            myStack.append(heights[counter])
                            if heights[counter] < minNum:
                                minNum = heights[counter]
                                indexOfMin = counter
                    elif heights[counter] < minNum:
                        minNum = heights[counter]
                        indexOfMin = counter
                        myStack.append(minNum)
                    else:
                        myStack.append(minNum)
                    counter+=1
                print(heights)
                height = self.findMaxHeight(myStack, minNum)
                if(height > maxHeight):
                    maxHeight = height
                heights[indexOfMin] = 0
                
            return maxHeight


    def findMaxHeight(self, stack, min):
        max = 0
        for item in stack:
            if item != 0:
                max += min
        return max
    

test = BarGraph()
list = [2,1,5,6,2,3]
print(test.largestRectangleArea(list))