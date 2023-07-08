class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # first attempt: is this just combinations? most have 3 letters but 7 and 9 have 4.
        # what if we just append the first letter to how many we have then the second and so on
        # Use dixtionary
    

        if digits == "":
            return []

        arr = []

        letters = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz",
        }

        # found out this is a backtracking problem
        def backtrack(index, currStr):
            if len(currStr) == len(digits): # if we have enough characters
                arr.append(currStr)         # append it
                return                      
            
            for char in letters[digits[index]]:     # for every character assigned to a digit
                backtrack(index+1, currStr + char)  # gets called exponentially 3 times for every letter

                

        backtrack(0,"")


        return arr


