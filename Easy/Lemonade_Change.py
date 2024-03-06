class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # first attempt: keep a list of all the bills I have and take from there using greedy
        # dictionary might be faster to look through to see if we have bills
        # might be faster to not even calculate it, could just look through the array

       
        myBills = {
            "5":0,
            "10":0,
        }

        for i in range(0, len(bills)):
            if bills[i] == 5:
                myBills["5"] += 1
                continue
            if bills[i] == 10:
                if myBills["5"] > 0:
                    myBills["5"] -= 1
                    myBills["10"] += 1
                    continue
                else:
                    return False
                
            if myBills["10"] > 0:
                myBills["10"] -= 1
                if myBills["5"] > 0:
                    myBills["5"] -= 1
                else:
                    return False
            else:
                if myBills["5"] > 2:
                    myBills["5"] -= 3
                else:
                    return False



        return True