class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # idea: greedy and we sort from least to greatest and then just do whatever overlaps from left to right
        arrows = 1
        sorted_list= sorted(points, key=lambda x: x[0])
        print(sorted_list)
        original_balloon = 0
        for i in range(0, len(sorted_list)):
            if(sorted_list[original_balloon][1] >= sorted_list[i][0]):
                # combine both into one arrow
                if(sorted_list[original_balloon][1] > sorted_list[i][1]): # if ending state of original is greater than ending state of new balloon
                    original_balloon = i
            else:
                arrows+=1
                original_balloon=i

        # if(original_balloon != len(sorted_list)-1):
        #     arrows+=1

        return arrows