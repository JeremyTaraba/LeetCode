"""
Prompt:
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.


"""



class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
    
        wordList = []
        strings = s.split(" ")        
        for eachWord in strings:
            wordList.append(eachWord[::-1])

        finalString = " ".join(wordList) # Join all items from list into a string, using a space as separator:
        return finalString

"""
Notes:
O(n) runtime
first split each string on spaces to get each word. Then reverse each word in to a list. 
Then using the list, join each word with a space as a separator into the final string

Constraints:
1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.

"""