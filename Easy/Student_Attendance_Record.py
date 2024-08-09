class Solution:
    def checkRecord(self, s: str) -> bool:
        # O(n) runtime to go through all characters and O(1) space

        absent = 0
        lateInRow = 0

        for char in s:
            if char == 'A':
                absent+=1
                lateInRow = 0
            if char == 'L':
                lateInRow+=1
                if lateInRow == 3:
                    return False
            else:
                lateInRow = 0
            

        return absent < 2