class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # [jfk] - [sfo, atl]
        # [sfo] - [atl]
        # [atl] - [jfk, sfo]
        # remove all values
        # backtracking?
        res = []
        hashMap = defaultdict(list)
        
        for key, value in sorted(tickets)[::-1]:
            hashMap[key].append(value)


        def dfs(src):
            while hashMap[src]:
                dst = hashMap[src].pop()
                dfs(dst)
            res.append(src)



        dfs("JFK")
        return res[::-1]


