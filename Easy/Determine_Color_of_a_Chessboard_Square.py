class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        
        c = ord(coordinates[0]) - 96
        coordinates = str(c) + coordinates[-1:]
        
        
        first = int(coordinates[0]) % 2 == 0      
        second = int(coordinates[1]) % 2 == 0
            
        return first != second  # logical xor gate


"""
Notes:
We have a string "a1", think of this in terms of numbers we have odd numbers being false and even
numbers being true. First I convert the first character in the string 'a' to a number. where a = 1, b = 2
and so on. Our new string is "11" check each number to see if it is even or odd. Two odd numbers is a black square
two even numbers is a black square and an odd and even number will always be a white square. This is a Xor operation.


Constraints:
coordinates.length == 2
'a' <= coordinates[0] <= 'h'
'1' <= coordinates[1] <= '8'

"""