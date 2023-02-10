class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # first attempt: check if character is in string
        # if not then that is the added character
        # the "in" operator checks for membership. it is a combination of 
        # boyer-moore and horsepool algorithms O(nm) in worst case and O(m/n) is best

      """
        test = t
        for i in t:
            if(i in s):
                test = test.replace(i, '')  # remove the character from s
        
        return test
        """

        # ^ wasn't working for some reason?? using counters instead which is just
        # dictionary where the value tells how many of that object is there


      
        s = Counter(s)
        t = Counter(t)

        addLetter = t-s  # dictionary with difference between the 2 dictionaries
        return list(addLetter.keys())[0]