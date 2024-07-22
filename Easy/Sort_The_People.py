class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # this is just sorting and moving the list of names the same way. 
        # would take O(N log N) to do this
        # could also make a pair out of these lists and sort the pair based on height

        # making our pair
        pairs = []
        for i in range(0, len(names)):
            tupl = (names[i], heights[i])
            pairs.append(tupl)
        
        # sorting the pair based on height
        pairs.sort(reverse = True,key=operator.itemgetter(1))

        # returning the pair decoupled
        return list(list(zip(*pairs))[0])


        