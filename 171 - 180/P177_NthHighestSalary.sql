######################################################

#   Solved on Friday, 28 - 01 - 2022.

######################################################


######################################################

#   Runtime: 292ms   -   80.97%
#   Memory: 0B  -   100.00%

######################################################

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  # We set N to N - 1 here because, LIMIT is 0 based. So LIMIT N, 1 will give us
  # (N+1)st largest salary instead of Nth largest. We can't give LIMIT N-1,1 in the
  # query. So we are creating this here
  SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      # Since we need Nth unique largest salary, we added DISTINCT
      SELECT DISTINCT salary 
      FROM Employee
      ORDER BY salary DESC
      LIMIT N, 1
  );
END