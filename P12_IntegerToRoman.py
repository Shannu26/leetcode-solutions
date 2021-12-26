######################################################

#   Solved on Saturday, 27 - 11 - 2021.

######################################################


######################################################

#   Runtime: 36ms   -   98.71%
#   Memory: 14.1MB  -   95.41%

######################################################

class Solution:
    def intToRoman(self, num: int) -> str:
        # The possible roman number instances in order of value
        pairs = [
                    ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
                    ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
                    ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
                ]
        
        romanNumber = ""
        # We loop through the pairs and if the number corresponding to a pair i.e;
        # pair[1] gives quotient > 0 if we divide num by it, then we need to add 
        # the string corresponding to pair i.e; pair[0] quotient number of times to
        # requried romanNumber string.
        # Then we take the remainder we get and store it in num, by doing
        # num = num % pair[1]
        # Example: 33
        # 23 // 10 == 3. So we add 'X' which is the roman value of 10, 2 times to get
        # 'XX'. And num = 23 % 10 == 3.
        # Then, 3 // 1 == 3. So we add 'I' which is the roman value of 1, 3 times to
        # get 'XXIII' 
        for pair in pairs:
            if num // pair[1] != 0:
                romanNumber += pair[0] * (num // pair[1])
                num = num % pair[1]
        
        return romanNumber