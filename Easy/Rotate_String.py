class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if(len(s) != len(goal)):
            return False

        sDouble = s+s
        return goal in sDouble