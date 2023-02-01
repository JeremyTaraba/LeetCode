class Solution:
    def intToRoman(self, num: int) -> str:
        # first attempt: Recursively subtract the largest roman numeral you can from the num
        # Does it need to be recursive? is it simpler to use while loop?

        # second attempt: Use a dictionary instead of 2 lists and see size difference
        # also instead of having if statements for special cases, add those into the
        # dictionary as their own characters

        # ans = ""
        # values = [1000, 500, 100, 50, 10, 5, 1]  # only 7 roman numerals
        # romanNums = ["M", "D", "C", "L", "X", "V", "I"]

        # for i in range(0, len(values)):
        #     while(num - values[i] >= 0):  # loops 7*n = O(7n)
        #         ans += romanNums[i]
        #         num -= values[i]
        #     if(num - values[i] < 0): # check special cases
        #         if(num == 4):
        #             ans += "IV"
        #             num -= 4
        #         elif(num == 9):
        #             ans += "IX"
        #             num -= 9
        #         elif(num >= 40 and num < 50):
        #             ans += "XL"
        #             num -= 40
        #         elif(num >= 90 and num < 100):
        #             ans += "XC"
        #             num -= 90
        #         elif(num >= 400 and num < 500):
        #             ans += "CD"
        #             num -= 400
        #         elif(num >= 900 and num < 1000):
        #             ans += "CM"
        #             num -= 900

    # Second attempt-------------------------------------------------------------
    # a bit faster and easier to understand than 2 lists
        ans = ""
        romanNums = {
            "M" : 1000,
            "CM" : 900,
            "D" : 500,
            "CD" : 400,
            "C" : 100,
            "XC" : 90,
            "L" : 50,
            "XL" : 40,
            "X" : 10,
            "IX" : 9,
            "V" : 5,
            "IV" : 4,
            "I" : 1,
        }

        for key in romanNums:
            while(num - romanNums[key] >= 0):
                ans += key
                num -= romanNums[key]
                


        return ans