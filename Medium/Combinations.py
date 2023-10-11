class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # first attempt: should be n^k-n operations at least
        list = []
        if k == 1:      # basecase, k >= 1 and so is n, program could run fine without it but I found it is faster with it
            for i in range(n):
                list.append([i+1])
            return list

        def backtracking(start, combination):
            if len(combination) == k:
                list.append(combination.copy())
                return
            
            for i in range(start,n+1):
                combination.append(i)
                backtracking(i+1,combination)
                combination.pop()
        
        
        backtracking(1,[])
        return list

        