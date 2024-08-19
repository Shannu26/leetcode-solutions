######################################################

#   Solved on Wednesday, 11 - 08 - 2023.

######################################################


######################################################

#   Runtime: 739ms   -   76.34%
#   Memory: 36.07MB  -   84.36%

######################################################

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
            The logic is to use Monotonic Stack.
            To begin with we sort the speed and position arrays based on descending order of position
            i.e; car closer to the target comes first in the arrays.
            Now, we loop through them and find time taken by that car to reach target and we time to stack.
            Now, let's say car at position p1 reaches target in time t1 and car at position p2 reaches
            target in time t2
                - If p1 > p2 and t1 < t2, then car c1 reaches the target before c2. Since c2 is behind
                c1, there won't be any collision. So, nothing to do
                - If p1 > p2 and t1 > t2, then car c2 reaches target before c1. Since c2 is behind c1,
                c2 collides with c1 at some point, they become car fleet and both reaches target at
                same time which is t1. So, at this point if t1 > t2 we don't care about t2 since it will
                anyway become t1 at some point. So, we pop t2 from stack.
            Number of car fleets == number of different reach times of cars which is stored in stack.
        """
        # Creating and Sorting
        speedPosition = [(speed[index], position[index]) for index in range(len(position))]
        speedPosition.sort(key = lambda x: -x[1])
        stack = []
        # Looping
        for speed, position in speedPosition:
            time = (target - position) / speed
            stack.append(time)
            # Checking for condition 2 mentioned above and if that condition is true, popping t2
            if len(stack) >= 2 and stack[-1] <= stack[-2]: stack.pop()
        
        return len(stack)