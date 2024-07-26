class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # count how many folder we go in -> */
        # count how many ../ we have
        # find the difference

        back=0
        forward=0
        for log in logs:
            if log == "../":
                if back < forward:
                    back+=1
            elif log == "./":
                pass
            else:
                forward+=1
        
        return forward - back 
