######################################################

#   Solved on Thursday, 17 - 03 - 2022.

######################################################


######################################################

#   Approach I  -  With Loop

#   Runtime: 20ms   -   99.77%
#   Memory: 13.8MB  -   97.30%

######################################################

class Solution:
    def totalMoney(self, n: int) -> int:
        """
            On 1st monday he credits 1$ into bank
            On all next monday's he credits 1$ more than previous monday
            On all remaining days he credits 1$ more than previous day

            So if we consider each week separately, we can see that each week
            is in arithmetic progression where start value a == how much he invests
            on monday, n == 7 since each week has 7 days and d == 1 since each day
            we only invest 1$ more than prev day.
            Formula to sum of n values in arithemetic progresion is
                    (n / 2) * (2a + (n - 1)d)
            So, to find how much we invest in a week formula is
                    (7 / 2) * (2a + (7 - 1)1)
                    (7 / 2) * (2a + 6)
            This logic is valid till n >= 7, since if n < 7 we don't have 7 days
            in that last week
            In that last week we will have only n days instead of 7, so formula is
                    (n / 2) * (2a + (n - 1))
        """
        total = 0
        # To keep track of how much we invest on monday of each week
        start = 1
        # While there are still full week left
        while n >= 7:
            # Using (7 / 2) * (2a + 6) to find total we invest in that week where
            # a == start
            total += (7 * ((2 * start) + 6)) // 2
            # One week done. So reducing n by 7 and in next week monday we invest
            # 1$ dollar than this week. So increase start by 1
            n -= 7
            start += 1
        # We have 0 to 6 days left. So using (n / 2) * (2a + (n - 1)) to find total
        # we invest in those last n days
        total += (n * ((2 * start) + (n - 1))) // 2
        
        return total

######################################################

#   Approach II  -  Without Loop

#   Runtime: 20ms   -   99.77%
#   Memory: 13.8MB  -   97.30%

######################################################

class Solution:
    def totalMoney(self, n: int) -> int:
        """
            We can simplify above approach to no loop if we observe carefully
            Loop runs as long as n >= 7 right.
            Each time we are adding (7 / 2) * (2a + 6)
                                === 7a + 21
            This runs lets say k times where the only thing that changes is 'a'
            which becomes a + 1 every next time.
            If we want to do it in single line without loop
            (7a + 21) + (7(a+1) + 21) + (7(a+2) + 21) + ....... k times
            Let's simplify it
            21 + 21 + .... k times === 21 * k ----> 1st step
            7a + 7(a+1) + 7(a+2) + ...... k times where starting a is 1
            So, 7 + 14 + ..... k times
                7 * (1 + 2 + ... k)
                Sum of k natural number is k * (k+1) / 2
                7 * k * (k+1) / 2 ----> 2nd step

            After that loop we have < 7 days right and start will be 1 greater
            than previous week start. We start at 1 and have k weeks. So, for
            (k+1)th week we have start == k+1
            We have r remaining days. Sum formuls is
                    (r/2) * (2(k+1) + (r-1)) ----> 3rd step

            If we observe k will be n // 7 since how many times we can divide
            n by 7 is the value of full weeks
            and r == n % 7
        """
        # k value
        numOfFullWeeks = n // 7
        # r value
        remainingDays = n % 7
        # 1st step
        total = 21 * numOfFullWeeks
        # 2nd step
        total += 7 * numOfFullWeeks * (numOfFullWeeks + 1) // 2
        # 3rd step
        total += (remainingDays * ((2 * (numOfFullWeeks + 1)) + (remainingDays - 1))) // 2
        
        return total