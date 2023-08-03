######################################################

#   Solved on Wednesday, 15 - 12 - 2021.

######################################################


######################################################

#   Runtime: 29ms   -   77.68%
#   Memory: 14MB  -   99.29%

######################################################

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # If dividend is 0, quotient will always be 0 since 0 divided by any number
        # is 0
        if dividend == 0: return 0
        # This is required because max +ve value of integer in java and c is 
        # 2147483647 and max -ve value is -2147483648. If dividend is -ve max value
        # and if divisor is -1, we will get 2147483648 as quotient. But it exceeds
        # the +ve limit of integer. So we return 2147483647
        if dividend == -2147483648 and divisor == -1: return 2147483647
        # Determining the sign of result
        sign = 1
        # If dividend is -ve, we multiply sign by -1 and we change dividend to +ve
        if dividend < 0: 
            sign = -1 * sign
            dividend = -1 * dividend
        # If divisor is -ve, we multiply sign by -1 and we change divisor to +ve
        if divisor < 0:
            sign = -1 * sign
            divisor = -1 * divisor
        
        quotient = 0
        # If dividend < divisor, divisor can't divide dividend anymore. So we loop
        # as long as dividend >= divisor
        while dividend >= divisor:
            # k is used to determine how many times we need to multiply divisor by 2
            # Logic is, we will consider even multiples of divisor as long as divisor
            # <= dividend. If it becomes > dividend, then we will get the quotient as
            # 2 ^ k
            # We subtract the multiple of divisor which is just below the multiple 
            # that became > dividend from dividend
            # a << b will add 0 bits b number of times to a to the right end. 
            # i.e; 2 << 2 will be 1000 since 2 == 10 in binary and adding 2 0 bits 
            # at end will make it 1000 which is 8 

            # Example, dividend = 10 and divisor = 3
            k = 0
            # k = 0, dividend = 10 > (divisor << 1 = 6)
            # k = 1, dividend = 10 < (divisor << 2 = 12)
            while dividend > divisor << (k + 1): k += 1
            # quotient += 1 << 1 === quotient += 2 [10 in binary]
            # quotient = 2
            quotient += 1 << k
            # dividend -= 3 << 1 === dividend -= 6 [110 in binary]
            # dividend = 4
            dividend -= divisor << k
        
        return quotient * sign