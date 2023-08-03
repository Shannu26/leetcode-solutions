######################################################

#   Solved on Sunday, 02 - 01 - 2022.

######################################################


######################################################

#   Runtime: 40ms   -   88.05%
#   Memory: 14.1MB  -   98.09%

######################################################

class Solution:
    def countAndSay(self, n: int) -> str:

        string = "1"
        
        for i in range(1, n):
            nextStr = ""
            # We initialise count to 1, because char at string[0] has occured one time
            # i.e; at 0th index.
            count = 1
            char = string[0]
            
            for j in range(1, len(string)):
                # If char at string[j] matches with char, we increase that char count
                # by 1
                if string[j] == char: count += 1
                # If they don't match, count will have how many times char has appeared
                # contiguous till j - 1th index and char will have the character
                # So we add str(count) + char to existing nextStr
                else:
                    nextStr += str(count) + char
                    char = string[j]
                    # Why count = 1 is chat at string[j] != string[j - 1]. So, we are
                    # starting newly at jth index. But in next iteration j becomes
                    # j + 1. So, since char at string[j] has occured once we initialise
                    # count with 1
                    count = 1
            # Adding last contiguous character count to nextStr
            nextStr += str(count) + char
            # Storing nextStr value in string
            string = nextStr
        
        # string will have the count and say value of n
        return string
        