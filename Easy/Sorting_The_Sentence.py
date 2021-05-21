class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        str1=s.split()
        orderList=[""]*len(str1)
        for word in str1:
            justString=word[:-1] #remove last character which is number
            orderList[int(word[-1])-1]=justString   #str[-1] goes to last character in string
            ans=" ".join(orderList)

        return ans