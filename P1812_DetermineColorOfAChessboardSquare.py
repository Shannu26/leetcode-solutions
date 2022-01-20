######################################################

#   Solved on Wednesday, 19 - 01 - 2022.

######################################################


######################################################

#   Runtime: 26ms   -   84.10%
#   Memory: 14.1MB  -   90.41%

######################################################

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # Ascii value of 'a' is 97
        # Ascii value of '1' is 49
        # We know that chess board has black and white squares alternatively
        # 'a1' is black. ascii(a) + ascii(1) = 97 + 49 = 146. So, 146 which is even
        # has black. So, 147 which is odd will have white
        # From this we can say that cells having sum of ascii value of char and num
        # odd will have white color
        # So, we find sum of char and num of given cell and get remainder when we 
        # divide by 2 and return it
        return (ord(coordinates[0]) + ord(coordinates[1])) % 2
