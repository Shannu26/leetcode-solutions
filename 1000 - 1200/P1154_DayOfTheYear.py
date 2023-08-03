######################################################

#   Solved on Thursday, 20 - 01 - 2022.

######################################################


######################################################

#   Runtime: 56ms   -   97.99%
#   Memory: 14.1MB  -   83.26%

######################################################

class Solution:
    def dayOfYear(self, date: str) -> int:
        
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[-2:])
        # Initializing dayNumber with day, since we are at 'day' in the 'month'
        # We just need to find how many days there are in month 1 till prev month
        dayNumber = day
        # Looping from month 1 to current month - 1, since March 1st means
        # February is completed but not March, we shouldn't add number of days in
        # March to our result
        for mon in range(1, month):
            # mon == 2 means it is February. It has min of 28 days in all years. So,
            # we add it to dayNumber
            if mon == 2: 
                dayNumber += 28
                # Then, we check if current year is leap year. If it is a leap year
                # we have 29 days in February. So, we add 1 to dayNumber
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): dayNumber += 1
            else:
                # If mon is not February, each month will have min of 30 days.
                dayNumber += 30
                # If we observe, From Month 1 to Month 7, odd months have 31 days
                # From month 8 to 12, even months have 31 days. So, we are checking
                # if any of these two is true. If yes, we are adding 1 to dayNumber
                if (mon < 8 and mon % 2 != 0) or (mon > 7 and mon % 2 == 0): dayNumber += 1
        
        return dayNumber