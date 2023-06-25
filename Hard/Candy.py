class Solution:
    def candy(self, ratings: List[int]) -> int:
        # first attempt: cant change the order, two pointers? check if neighbor is bigger or smaller
        # would knowing min or max value help? min would help because you know to give them 1
        # keep track of what the previous kid got
        # create second list to keep track of if it went up or down

        
        # if(len(ratings) == 1):  # can't be zero per constraints
        #     return 1
        

        # totalCandy = 0
        # if(len(ratings) > 2):
        #     curr = ratings[0]
        #     next = ratings[1]
        #     min = 0
        #     prev = 1

        #     for i in range(len(ratings)-1):
        #         if curr > next:
        #             print()
        #         elif curr < next:
        #             print()
        #         else:
        #             print()


        

        # return totalCandy



        # ^ couldn't get it to work

        # second attempt: Use 2 passes, will need another array. 