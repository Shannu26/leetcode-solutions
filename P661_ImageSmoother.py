######################################################

#   Solved on Saturday, 15 - 01 - 2022.

######################################################


######################################################

#   Runtime: 628ms   -   83.55%
#   Memory: 14.9MB  -   82.69%

######################################################

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        smoothedImg = [[img[i][j] for j in range(len(img[0]))] for i in range(len(img))]
        
        for i in range(len(img)):
            for j in range(len(img[0])):
                # Size is initialized with 1 because, smoothedImg is initialized as a
                # copy of img. sot smoothedImg[i][j] has img[i][j]. So the min size is
                # 1
                size = 1
                # Top cell
                if i - 1 != -1:
                    size += 1
                    smoothedImg[i][j] += img[i - 1][j]
                # Top-Left cell
                if i - 1 != -1 and j - 1 != -1:
                    size += 1
                    smoothedImg[i][j] += img[i - 1][j - 1]
                # Top-Right cell
                if i - 1 != -1 and j + 1 != len(img[0]):
                    size += 1
                    smoothedImg[i][j] += img[i - 1][j + 1]
                # Left cell
                if j - 1 != -1:
                    size += 1
                    smoothedImg[i][j] += img[i][j - 1]
                # Bottom-Left cell
                if i + 1 != len(img) and j - 1 != -1:
                    size += 1
                    smoothedImg[i][j] += img[i + 1][j - 1]
                # Right cell
                if j + 1 != len(img[0]):
                    size += 1
                    smoothedImg[i][j] += img[i][j + 1]
                # Bottom cell
                if i + 1 != len(img):
                    size += 1
                    smoothedImg[i][j] += img[i + 1][j]
                # Bottom-right cell
                if i + 1 != len(img) and j + 1 != len(img[0]):
                    size += 1
                    smoothedImg[i][j] += img[i + 1][j + 1]
                smoothedImg[i][j] //= size
        
        return smoothedImg