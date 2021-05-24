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