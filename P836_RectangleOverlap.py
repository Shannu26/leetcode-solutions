######################################################

#   Solved on Wednesday, 20 - 01 - 2022.

######################################################


######################################################

#   Runtime: 24ms   -   96.25%
#   Memory: 14MB  -   98.21%

######################################################

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Instead of checking if they overlap, it is easier to check if they don't 
        # overlap. If they don't overlap, rec1 will be to left or right or top or 
        # bottom of rec2
        # Given (x1,y1,x2,y2) where x1,y1 is bottom-left corner of rectangle
        # and x2,y2 is top-right corner of rectangle.
        # rec1 will be to left of rec2, if x index of 2 corner of rec1 are < bottom
        # -left index of rec2. Since, bottom-left corner of rec1 is already to left
        # of top-right corner, we just have to check if top-right corner of rec1 <=
        # bottom-left corner of rec2
        #           rec1[2] <= rec2[0]
        # Similarly, rec1 will be to bottom of rec2, if y index of top-right corner of
        # rec1 <= y index of bottom-left corner of rec2
        # rec1 will be to right of rec2, if x index of bottom-left corner of rec1 >=
        # x index of top-right corner of rec2
        # rec1 will be to top of rec2, if y index of bototm-left corner of rec1 >=
        # y index of top-right corner of rec2
        # If any of these cases are true, then we can say that both rectangles don't
        # overlap. So, we return NOT of OR of all these cases
        return not (
            rec1[2] <= rec2[0] or # Left Case
            rec1[3] <= rec2[1] or # Bottom Case
            rec2[2] <= rec1[0] or # Right Case
            rec2[3] <= rec1[1] # Top Case
        )