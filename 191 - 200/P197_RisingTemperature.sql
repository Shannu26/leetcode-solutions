######################################################

#   Solved on Friday, 28 - 01 - 2022.

######################################################


######################################################

#   Runtime: 433ms   -   60.90%
#   Memory: 0B  -   100.00%

######################################################

# Write your MySQL query statement below
SELECT weather1.id as id
FROM Weather weather1
JOIN Weather weather2
WHERE (
    DATEDIFF(weather1.recordDate, weather2.recordDate) = 1
    AND
    weather1.temperature > weather2.temperature
    );