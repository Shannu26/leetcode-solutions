######################################################

#   Solved on Tuesday, 15 - 02 - 2022.

######################################################


######################################################

#   Runtime: 124ms   -   97.37%
#   Memory: 16.3MB  -   98.38%

######################################################

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
            We use XOR operation to do this problem using O(1) space and O(n)
            time complexity.
            Truth Table of XOR is
                A   B   A^B
                0   0    0
                0   1    1
                1   0    1
                1   1    1
            We can see that if A and B have same bit we will get 0 as answer
            So, lets consider example [4, 1, 2, 1, 2]
            In binary they are [100, 001, 010, 001, 010]

            What we do is find XOR of all number in array and store it in number
            So,
                number = 100 ^ 001 ^ 010 ^ 001 ^ 010
            XOR is commutative. So A ^ B = B ^ A
            So, we consider above number operation in different order so that we
            can understand the logic
                number = 001 ^ 001 ^ 010 ^ 010 ^ 100
            XOR is associative. So A ^ (B ^ C) = (A ^ B) ^ C
                number = (001 ^ 001) ^ (010 ^ 010) ^ 100
            According to truth table above, if both A and B are same, we get 0. 
            So, if a numA = numB, we will get 0 as XOR.
                number = 000 ^ 000 ^ 100
            000 ^ 000 = 000
                number = 000 ^ 100
            From truth table of XOR, number = 100 ==> 4

            Therefore logic is to perfom XOR of all numbers and returning it
        """
        number = 0
        
        for num in nums:
            number = number ^ num
        
        return number