class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # reverse the list
        # increment the first value
        # see if there is a remainder and loop as long as remainder is there
        # reverse the list
        # return it

        
        digits.reverse()
        digits[0] +=1
        if digits[0] == 10:
            index = 0
            while digits[index] == 10 and index < len(digits)-1:
                digits[index] = 0
                digits[index+1] += 1
                index+=1
            if (len(digits)-1 == index and digits[index] == 10) or len(digits) == 1:
                digits[index] = 0
                digits.append(1)
        digits.reverse()
        return digits