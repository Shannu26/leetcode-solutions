######################################################

#   Solved on Friday, 28 - 01 - 2022.

######################################################


######################################################

#   Runtime: 215ms   -   99.76%
#   Memory: 0B  -   100.00%

######################################################

# Write your MySQL query statement below
SELECT Name, Population, Area
FROM World
WHERE (Area >= 3000000 OR Population >= 25000000);