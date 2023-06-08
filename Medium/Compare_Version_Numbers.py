class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # first attempt: split the version on "." and store sections into a list
        # compare indexes of the list against each other, ignoring leading 0's
        # what if versions have different number of "."? could pad with 0's and "."?

        list1 = version1.split(".")
        list2 = version2.split(".")

        ans = 0
        
        smallestLen = min(len(list1), len(list2))
        
        if(len(list1) > len(list2)):
            biggerList = 1
        elif(len(list1) < len(list2)):
            biggerList = 2
        else:
            biggerList = 0
        
        for i in range(smallestLen):
            if(int(list1[i]) > int(list2[i])):
                ans = 1
                break
            elif(int(list1[i]) < int(list2[i])):
                ans = -1
                break     


        if(biggerList != 0 and ans == 0):  # this is for differing number of "."
            if(biggerList == 1):
                for i in range(smallestLen,len(list1)):
                    if(int(list1[i]) != 0):
                        ans = 1
            else:
                for i in range(smallestLen,len(list2)):
                    if(int(list2[i]) != 0):
                        ans = -1

        
        return ans

        # ^ linear runtime 
