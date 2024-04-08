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

a = list(map(int, [1,2,3]))

b = list(map(int,  [0,2,3]))
compareTriplets(a,b)