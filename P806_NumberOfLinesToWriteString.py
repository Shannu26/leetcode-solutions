######################################################

#   Solved on Thursday, 27 - 01 - 2022.

######################################################


######################################################

#   Runtime: 24ms   -   97.63%
#   Memory: 13.8MB  -   99.57%

######################################################

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        # lines[0] will store how many lines are there
        # lines[1] will store pixels valus of last line
        lines = [0, 0]
        # Stores pixel value of each line
        pixels = 0
        
        for char in s:
            # If adding char to current line exceeds the max pixel length which
            # is 100, we go to next line, so we increase lines[0] by 1
            # In next line we write the current char, so pixels will be 
            # reinitialized with the pixel width of cuurent char
            if widths[ord(char) - 97] + pixels > 100:
                lines[0] += 1
                pixels = widths[ord(char) - 97]
            # Else, we add current char to current line and increase the pixels
            # to pixels + width of current char
            else:
                pixels += widths[ord(char) - 97]
        # After loop ends we haven't added last line. So we increase lines[0] by
        # 1 and pixels will have pixel value of last line. So we store it in 
        # lines[1]
        lines[0] += 1
        lines[1] = pixels
        return lines