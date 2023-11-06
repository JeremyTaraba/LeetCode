class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # first attempt: seems like we just need to check that it increases and decreases
        # can set a bool if it is increasing and another to check that it went from increasing to decreasing
        # then return that is was decreasing and it went from increasing to decreasing
        # O(n) runtime, O(1) space


        size = len(arr)

        if size < 3:
            return False



        increasing = False
        decreasing = False

        i = 1
        while i < size:
            if arr[i-1] < arr[i]:
                increasing = True
                if increasing and decreasing:
                    return False
            elif arr[i-1] == arr[i]:
                return False
            else:
                if increasing:
                   increasing = False 
                   decreasing = True
                elif not decreasing:
                    return False
            i+=1


        return (not increasing) and decreasing
        