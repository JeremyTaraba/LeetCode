class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # just math, for single value, will take value of ascii A - 64, 
        # double letter is value of 26 * value of first letter + value of second. 
        # triple letter is value of 26^2 * 26 * value of second letter + value of third and so on

        columnNumber = 0
        pos = 0
        for i in range(len(columnTitle)-1, -1, -1):
            digit = ord(columnTitle[i]) - 64
            columnNumber += digit * 26 ** pos
            pos += 1

        
            
            
        return columnNumber