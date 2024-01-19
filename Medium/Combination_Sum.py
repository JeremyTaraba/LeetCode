class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # first try: input seems to be ordered, if not then we can order it.
        # combination question will have bad runtime
        

        answerList = []
       

        def recursive(updatedTarget, index, potentialAnswer):  
            if updatedTarget < 0:
                return
            if updatedTarget == 0:
                answerList.append(potentialAnswer)
                return
            for i in range(index, len(candidates)):
                recursive(updatedTarget-candidates[i], i, potentialAnswer+[candidates[i]])
        recursive(target,0,[])
       
        return answerList