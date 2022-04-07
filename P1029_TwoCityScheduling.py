######################################################

#   Solved on Friday, 25 - 03 - 2022.

######################################################


######################################################

#   Runtime: 36ms   -   97.87%
#   Memory: 13.8MB  -   98.73%

######################################################

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
            Consider an example,
                [[10,20], [30,200], [40,500], [30, 20]]
            To begin with, let's assume that we send all the 2n candidates to city A
            only. Since, we have to send n people to city B let's consider the profit
            or loss we will be getting if a person in city A goes to city B
                Initially, 
                city A = [10, 30, 40, 30]
                city B = []

                If a person goes to city B instead of city A what is the profit/loss
                we will get. It is costOfA - costOfB right
                profit/loss = 
                    Person 1: 10 - 20 = -10 -> -ve means loss. So if person 1 goes to
                    city B instead of city A, we will have extra 10 cost of our travel

                    Person 2: 30 - 200 = -170 -> -ve means loss. So if person 2 goes to
                    city B instead of city A, we will have extra 170 cost of our travel

                    Person 3: 40 - 500 = -460 -> -ve means loss. So if person 3 goes to
                    city B instead of city A, we will have extra 460 cost of our travel

                    Person 4: 30 - 20 = 10 -> +ve means profit. So if person 4 goes to
                    city B instead of city A, we will save 10 cost of our travel

                We want to get minimum cost right. So we need to find the top n costs
                which have more loss if a person chooses city B instead of A so that
                we can send them to city A to avoid that loss.

                Sort the profit/loss in ascending order
                    -460        -170        -10         10
                Corresponding costs are
                    [40, 500]   [30, 200]   [10, 20]    [30, 20]

                The first n have more loss if we choose city B for them rather than
                city A. So we assign them to city A and last n to city B

                MinCost = 40 + 30 + 20 + 20
                           cityA     cityB
                             70   +   40
                                 110

        """
        # Sorting the costs based on loss we will get i.e; cost[0] - cost[1]
        costs.sort(key = lambda cost: cost[0] - cost[1])
        
        left = 0
        right = len(costs) - 1
        minCost = 0
        # Adding first n cityA costs and last n cityB costs
        while left < right:
            minCost += costs[left][0] + costs[right][1]
            left += 1
            right -= 1
        
        return minCost