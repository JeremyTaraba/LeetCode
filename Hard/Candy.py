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

   
        # second attempt: Use 2 passes, will need another array to keep track of what we have given
        # first give all kids 1 candy because they all get atleast one
        # next loop and if 1 kid is greater than the one before it then give him an extra 1 candy of what the kid before got
        # ex: 1,2,3 will be given 1,2,3 cadies
        # ex: 1,2,3,3 will be given 1,2,3,1 candies since from 3 to 3 it doesnt increase
        # Need a second pass for a case like 1,2,3,3,2 where they are given 1,2,3,2,1 

        length = len(ratings)
        arr = [1] * length
  
        # first pass goes forwards
        for i in range(length-1):       
            if ratings[i] < ratings[i+1]:
                arr[i+1] = arr[i] + 1
                
        
        # second pass goes backwards 
        for i in range(length-1, 0, -1):
            if ratings[i-1] > ratings[i] and arr[i-1] <= arr[i]:        # make sure to check that we actually need to add 1; arr[i-1] could already be more than arr[i]
                arr[i-1] = arr[i] + 1
                
                
        
        return sum(arr)
