"""
Prompt:
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

"""

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        str1=s.split()
        orderList=[""]*len(str1)
        for word in str1:
            justString=word[:-1]  #remove the last character which is the number
            orderList[int(word[-1])-1]=justString   #str[-1] goes to last character in string
            ans=" ".join(orderList)

        return ans


"""
Notes:
We create an empty list[] that has the size of how many words are in our sentence 
Then we place the words into the list based on their index.
O(n) time. 


Constraints:
2 <= s.length <= 200
s consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9.
The number of words in s is between 1 and 9.
The words in s are separated by a single space.
s contains no leading or trailing spaces.


"""