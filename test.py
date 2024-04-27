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

size = len(a)-1
quicksort(a,0,size)


latitude = "df"
longitude = "df"

try:
    with urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=282b9c5774fbbe93865898bfd449f756&units=imperial") as url:
        data = json.load(url)
    print(data)
except:
    print("error requesting weather from urllib")